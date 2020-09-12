from discord.ext import commands
from mojang import MojangAPI
import discord


@commands.command(
    name="skin",
    aliases=[],
    brief=("Returns a render of the specified player's skin, Defaults to full "
           "body render when no arguments are provided"),
    usage="<username> <head | face | bust | front | frontfull>"
)
async def skin(ctx, *args):
    try:
        playerName = args[0]
        playerUUID = MojangAPI.get_uuid(playerName)
        nameMC = ("[NameMC Profile](https://namemc.com/profile/"
                  f"{playerUUID})")

        if playerUUID is None:
            raise NameError

        if len(args) > 1:
            skinRender = (f"https://visage.surgeplay.com/{args[1]}/"
                          f"{playerUUID}.png")

        else:
            skinRender = (f"https://visage.surgeplay.com/full/512/{playerUUID}"
                          ".png")

        skinEmbed = discord.Embed(
            title=f"{playerName}'s Skin",
            description=nameMC,
            color=discord.Color.blue(),
        )
        skinEmbed.set_image(url=skinRender)

        await ctx.send(embed=skinEmbed)
    except Exception as e:
        print(e)
        errorEmbed = discord.Embed(
            title="Error",
            description="`⛔ Could not find a player"
                        f" with the name:{args[0]}`",
            color=discord.Color.red()
        )
        await ctx.send(embed=errorEmbed)


def setup(bot):
    bot.add_command(skin)
