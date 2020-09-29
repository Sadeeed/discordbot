from discord.ext import commands
import discord


@commands.command(
    name="donate",
    alias=["donation", "donations"],
    description=("Gives information on how to donate to the server. Provides "
                 "a link to the paypal site where donations can be made."),
    usage=''
)
async def donate(ctx):
    donateEmbed = discord.Embed(
        title="Paypal Donations",
        description=("Donations are never required but are "
                     "greatly appreciated."),
        color=discord.Color.green()
    )

    donateEmbed.add_field(name="To Donate:",
                          value=("[Click here](https://"
                                 "www.paypal.me/EbriusSMP)\n\nIf "
                                 "given the option please select*** "
                                 "Friends and Family*** when making "
                                 "a payment.This ensures Paypal does "
                                 "not take a cut of the payment and "
                                 "that the full amount will be "
                                 "received by us.\n\nDonating in ***"
                                 "Swedish Krona (SEK)*** is also "
                                 "preferred as this will prevent "
                                 "paypal from taking an exchange "
                                 "charge."),
                          inline=False)
    donateEmbed.add_field(name="\u200b",
                          value=("***Disclaimer:*** *Donating will "
                                 "not give you any extra perks or "
                                 "preferencial treatment.*"),
                          inline=False)

    await ctx.send(embed=donateEmbed)


def setup(bot):
    bot.add_command(donate)
