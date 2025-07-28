class Server:
    def __init__(self, id: str, name: str):
        """
        Initializes a Server instance.

        :param id: Unique identifier for the server.
        :param name: Name of the server.
        """
        self.id = id
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
