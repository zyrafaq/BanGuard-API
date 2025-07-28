class TerrariaPlayer:
    def __init__(self, id: str, latest_name: str, terraria_uuid: str, discord_id: int = None,
                 discord_account_name: str = None):
        """
        Initializes a TerrariaPlayer instance.

        :param id: Unique identifier for the player.
        :param latest_name: The latest name of the player.
        :param terraria_uuid: Unique Terraria hashed UUID for the player.
        :param discord_id: Optional Discord ID associated with the player.
        :param discord_account_name: Optional Discord account name associated with the player.
        """
        self.id = id
        self.latest_name = latest_name
        self.terraria_uuid = terraria_uuid
        self.discord_id = discord_id
        self.discord_account_name = discord_account_name

    def __str__(self):
        return self.latest_name

    def __repr__(self):
        return self.__str__()

    def has_connected(self) -> bool:
        return bool(self.discord_id)
