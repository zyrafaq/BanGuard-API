import datetime

from terraria_player import TerrariaPlayer


class ConnectionCode:
    """
    Represents a BanGuard Discord-Terraria connection code.
    """

    def __init__(self, code: str, player: TerrariaPlayer, expiration_timestamp: datetime.datetime, used: bool = False):
        """
        Initializes a ConnectionCode instance.

        :param code: The connection code.
        """
        self.code = code
        self.player = player
        self.expiration_timestamp = expiration_timestamp
        self.used = used

    def __str__(self):
        return str(self.code)

    def __repr__(self):
        return self.__str__()

    def is_expired(self) -> bool:
        """
        Checks if the connection code is expired.

        :return: True if expired, False otherwise.
        """
        return self.expiration_timestamp < datetime.datetime.now()
