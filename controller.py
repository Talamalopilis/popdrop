import discord
import helpers
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
                await self.client.send_message(self.message.channel,
                                               "Add a game with: `!popdrop addgame {game_name} {game_image_url} {max_players} {genre}`")
            else:
                await self.add_game(msg[2], msg[3], msg[4], msg[5])
        elif msg[1] == "pop":
            if len(msg) != 5:
                await self.client.send_message(self.message.channel, "Add a game session with:\n"
                                                                     "`!popdrop pop {game_name} {pick day: m,t,w,th,"
                                                                     "f,s,su}, {time: 8,9,etc}`\n" \
                                                                     "Example:\n`!popdrop pop Overwatch F 9`\n" \
                                                                     "Use `!popdrop games` to get a list of your server's games!")
            else:
                await self.add_session(msg[2], msg[3], msg[4])

    async def get_sessions(self):
        db = sessions.Sessions()
        out = db.get_active_sessions(self.message.server.id)
        if not out:
            await self.client.send_message(self.message.channel,
                                           "No sessions this week yet. Make one yourself with `!popdrop pop`!")
        for game_session in out:
            title, description, image = self.format_game(game_session[2])
            title += " this {} at {}!".format(helpers.get_day_from_date(game_session[4]), game_session[5])
            emb = discord.embeds.Embed(colour=0x00FF00, title=title, description=description)
            emb.set_image(url=image)
            await self.client.send_message(self.message.channel, embed=emb)

    async def get_all_games(self):
        db = games.Games()
        out = db.get_games(self.message.server.id)
        await self.client.send_message(self.message.channel, "Your server's available games: ```{}```"
                                                             "To get more info on a game use `!popdrop games {{game_name}}`.\n"
                                                             "To add a game use `!popdrop addgame`.".format(
            "\n".join(map(lambda x: x[0], out))))

    async def get_game(self, game_name):
        title, description, image = self.format_game(game_name)
        emb = discord.embeds.Embed(colour=0xFF4500, title=title, description=description)
        emb.set_image(url=image)
        await self.client.send_message(self.message.channel, embed=emb)

    def format_game(self, game_name):
        db = games.Games()
        data = db.get_game(game_name, self.message.server.id)
        title = data[0]
        description = "Maximum Players: ***{}***\nGenre: ***{}***".format(data[3], data[4])
        image = data[2]
        return (title, description, image)

    async def add_game(self, game_name, image_url, max_players, genre):
        db = games.Games()
        success = db.insert_game(game_name, self.message.server.id, image_url, max_players, genre)
        if success:
            await self.client.send_message(self.message.channel, "Successfully added game ***{}***!".format(game_name))
        else:
            await self.client.send_message(self.message.channel, "There was an error adding the game.")

    async def add_session(self, game_name, day_of_week, time_of_day):
        date_of_session = helpers.get_session_date(day_of_week.lower())
        db = sessions.Sessions()
        success = db.insert_session(self.message.server.id, game_name, date_of_session, time_of_day)
        if success:
            await self.client.send_message(self.message.channel,
                                           "Successfully added session for ***{}*** on ***{}***!".format(game_name,
                                                                                                         helpers.get_day_from_date(
                                                                                                             date_of_session)))
        else:
            await self.client.send_message(self.message.channel, "There was an error adding the session.")
