from discord.ext.commands import Bot

# client = discord.Client()
bot = Bot(command_prefix=">")

with open("token.txt") as fp:
    TOKEN = fp.read()


commands = ['plugins.help', 'plugins.skin']


@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    bot.remove_command('help')
    for command in commands:
        bot.load_extension(command)

bot.run(TOKEN)
