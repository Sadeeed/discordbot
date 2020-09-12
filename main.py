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


# @bot.listen("on_message")
# async def on_mention_reply_prefix(message: discord.Message) -> None:
#     """Replies the bot's prefix when mentioned"""
#     if bot.user.mentioned_in(message):
#         await message.channel.send(f"** Prefix is `{bot.command_prefix}`.**"
#                                    )


bot.run(TOKEN)
