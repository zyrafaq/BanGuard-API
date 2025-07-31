import asyncio
from banguardapi.async_client import Client


async def main():
    async with Client(token="token goes here") as client:
        player = await client.get_player("UUID goes here")

        print(player)
        ban = await client.ban_player(player, "griefing")
        print(ban)
        print(await client.unban_player(ban))
        print(await client.get_ban_categories())
        print(await client.get_ban_count())
        print(await client.new_connection_code(player))
        print(await client.check_connection_code("123456"))


if __name__ == "__main__":
    asyncio.run(main())