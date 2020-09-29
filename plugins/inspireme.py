from discord.ext import commands
import discord
import inspirobot


@commands.command(
    name="inspireme",
    alias=['inspiration', 'inspire', 'inspirobot'],
    description="Generates an inspiring image quote",
    usage=""
)
async def inspireme(ctx):
    imageURL = inspirobot.generate()
    inspireEmbed = discord.Embed(
        title="Inspiration",
        color=discord.Color.blue(),
    )
    inspireEmbed.set_image(url=imageURL)

    await ctx.send(embed=inspireEmbed)


def setup(bot):
    bot.add_command(inspireme)
