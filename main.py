from discord.ext.commands import Bot
import os
import json


def readConfig():
    with open("config.json") as f:
        config = json.load(f)
    return config


config = readConfig()

# client = discord.Client()
bot = Bot(command_prefix=config["commandPrefix"])

with open("token.txt") as fp:
    TOKEN = fp.read()


@bot.event
async def on_ready():
    # print('Logged in as {0.user}'.format(bot))
    print("\033[0;33m""▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬""\033[0m")
    print("\033[0;92m""{0.user} bot is online!""\033[0m".format(bot))
    print("\033[0;33m""▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬""\033[0m")
    bot.remove_command('help')
    for command in os.listdir("./plugins"):
        if command.endswith(".py"):
            print(f"[Loaded] {command}")
            bot.load_extension(f"plugins.{command[:-3]}")

bot.run(TOKEN)
