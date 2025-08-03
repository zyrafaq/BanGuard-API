from dataclasses import dataclass


@dataclass
class TerrariaPlayer:
    id: str
    latest_name: str
    terraria_uuid: str

    def __str__(self):
        return self.latest_name

    def __repr__(self):
        return self.__str__()
