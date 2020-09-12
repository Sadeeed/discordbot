from discord.ext import commands


@commands.command(
    name="help",
    aliases=[],
    brief="Shows this message"
)
async def help(ctx):
    await ctx.send("Prefix is >")


def setup(bot):
    bot.add_command(help)
