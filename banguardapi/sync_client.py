import requests

from ban import Ban
from connection_code import ConnectionCode
from exceptions import InvalidTokenError
from terraria_player import TerrariaPlayer


class Client:
    BASE_URL = "https://banguard.uk/api/"

    def __init__(self, token: str, check_token: bool = True):
        self._token = token
        self._session = requests.Session()
        self._session.headers.update({"Authorization": self._token})

        if check_token and not self.is_token_valid():
            raise InvalidTokenError()

    def _request(self, method: str, endpoint: str, **kwargs):
        """Helper method to send requests and handle errors."""
        url = f"{self.BASE_URL}{endpoint}"
        response = self._session.request(method, url, **kwargs)

        try:
            response.raise_for_status()
            data = response.json()
        except requests.HTTPError as e:
            try:
                error_msg = response.json().get("error", str(e))
            except Exception:
                error_msg = str(e)
            raise Exception(error_msg)
        except ValueError:
            raise Exception("Invalid JSON response")

        if "error" in data:
            raise Exception(data["error"])

        return data

    def is_token_valid(self) -> bool:
        """Return True if the token is valid, False otherwise."""
        data = self._request("GET", "check-token")
        return data.get("valid", False)

    def get_ban_count(self) -> int:
        """Fetch ban count from the BanGuard API"""
        data = self._request("GET", "ban-count")
        return data.get("ban_count", 0)

    def ban_player(self, player: TerrariaPlayer, category: str) -> Ban:
        """Ban a player"""
        data = {
            "player_uuid": player.terraria_uuid,
            "category": category,
        }
        response = self._request("POST", "ban-player", data=data)
        return Ban(response["ban"]["id"], player, category)

    def get_player(self, player_uuid: str) -> TerrariaPlayer:
        """Fetch a player from the API"""
        data = {
            "player_uuid": player_uuid,
        }
        response = self._request("POST", "get-player", data=data)
        return TerrariaPlayer(response["player"]["id"], response["player"]["latest_name"], player_uuid,
                              discord_id=response["player"]["discord_id"],
                              discord_account_name=response["player"]["discord_account_name"])

    def new_connection_code(self, player: TerrariaPlayer) -> ConnectionCode:
        """Create a new connection code for a player"""
        data = {
            "player_uuid": player.terraria_uuid,
        }
        response = self._request("POST", "new-connection-code", data=data)
        return ConnectionCode(response["code"], player, response["expiration_time"])

    def check_connection_code(self, code: str) -> bool:
        response = self._request("GET", "check-code", params={"code": code})
        return bool(response["valid"])

    def get_ban_categories(self) -> list:
        """Fetch the list of ban categories from the API"""
        return self._request("GET", "ban-category-list")["ban_categories"]
