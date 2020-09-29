from discord.ext import commands
import discord


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
        value="survival.ebrius.xyz",
        inline=False)
    ipEmbed.add_field(
        name="Creative",
        value="creative.ebrius.xyz",
        inline=False)
    ipEmbed.add_field(
        name="Events",
        value="jefflurr.beastmc.com",
        inline=False)

    await ctx.send(embed=ipEmbed)


def setup(bot):
    bot.add_command(ip)
