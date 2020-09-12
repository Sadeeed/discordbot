from discord.ext import commands
from mojang import MojangAPI


@commands.command(
    name="skin",
    aliases=[],
    brief="Returns a render of the specified player's skin, " +
    "Defaults to full body render when no arguments are provided",
    usage="<username> <head | face | bust | front | frontfull>"
)
async def skin(ctx, *args):
    uuid = MojangAPI.get_uuid(args[1])
    await ctx.send(uuid)


def setup(bot):
    bot.add_command(skin)
