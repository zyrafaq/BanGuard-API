from banguardapi.sync_client import Client


client = Client(token="token goes here")

player = client.get_player("UUID goes here")

print(player)
ban = client.ban_player(player, "griefing") # Example category. You can find a full list here: https://banguard.uk/ban-categories/
print(ban)
print(client.unban_player(ban))
print(client.get_ban_categories())
print(client.get_ban_count())
print(client.new_connection_code(player))
print(client.check_connection_code("123456"))
