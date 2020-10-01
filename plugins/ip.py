from discord.ext import commands
import discord
import main as m

config = m.readConfig()


@commands.command(
    name="ip",
    alias=['ips', 'server', 'servers'],
    description="Returns the IPs of Ebrius' Servers",
    usage=""
)
async def ip(ctx):
    ipEmbed = discord.Embed(
        title="Server IPs",
        color=discord.Color.green
    )

    ipEmbed.add_field(
        name="Survival",
        value=config['survivalIP'],
        inline=False)
    ipEmbed.add_field(
        name="Creative",
        value=config['creativeIP'],
        inline=False)
    ipEmbed.add_field(
        name="Events",
        value=config['eventsIP'],
        inline=False)

    await ctx.send(embed=ipEmbed)


def setup(bot):
    bot.add_command(ip)
