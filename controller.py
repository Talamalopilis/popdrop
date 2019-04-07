import discord
from db import games, sessions, subscriptions


class Controller:
    def __init__(self, client, message):
        self.client = client
        self.message = message

    async def on_message(self):  # !popdrop...
        msg = self.message.content.split(' ')
        if len(msg) == 1:
            await self.get_sessions()
        elif msg[1] == "games":
            if len(msg) == 2:
                await self.get_all_games()
            else:
                await self.get_game(msg[2])
        elif msg[1] == "addgame":
            if len(msg) != 6:
                await self.client.send_message(self.message.channel, "Add a game with: `!popdrop addgame {game_name} {game_image_url} {max_players} {genre}`")
            else:
                await self.add_game(msg[2], msg[3], msg[4], msg[5])

    async def get_sessions(self):
        pass

    async def get_all_games(self):
        db = games.Games()
        out = db.get_games(self.message.server.id)
        await self.client.send_message(self.message.channel, "Your server's available games: ```{}```".format("\n".join(map(lambda x: x[0], out))))

    async def get_game(self, game_name):
        db = games.Games()
        out = db.get_game(game_name, self.message.server.id)
        await self.client.send_message(self.message.channel, out)

    async def add_game(self, game_name, image_url, max_players, genre):
        db = games.Games()
        success = db.insert_game(game_name, self.message.server.id, image_url, max_players, genre)
        if success:
            await self.client.send_message(self.message.channel, "Successfully added game {}".format(game_name))
        else:
            await self.client.send_message(self.message.channel, "There was an error adding the game.")
