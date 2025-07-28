from server import Server
from terraria_player import TerrariaPlayer


class Ban:
    def __init__(self, player: TerrariaPlayer, server: Server, category: str):
        """
        Initializes a Ban instance.

        :param player: The player being banned.
        :param server: The server from which the player is banned.
        :param category: The BanGuard ban category.
        """
        self.player = player
        self.server = server
        self.category = category

    def __str__(self):
        return f"Ban(player={self.player}, server={self.server}, category={self.category})"

    def __repr__(self):
        return self.__str__()
