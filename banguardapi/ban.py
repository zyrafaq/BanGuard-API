from server import Server
from terraria_player import TerrariaPlayer


class Ban:
    def __init__(self, id, player: TerrariaPlayer, category: str, server: Server=None):
        """
        Initializes a Ban instance.

        :param id: Unique identifier for the ban.
        :param player: The player being banned.
        :param category: The BanGuard ban category.
        :param server: The server from which the player is banned.
        """
        self.id = id
        self.player = player
        self.server = server
        self.category = category

    def __str__(self):
        return f"Ban(player={self.player}, server={self.server}, category={self.category})"

    def __repr__(self):
        return self.__str__()
