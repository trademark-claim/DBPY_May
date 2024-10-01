from disnake.ext import commands
import disnake
from Utilities.staffchecks import modcheck
from Utilities.discord_utils import create_embed
maybot = None

@commands.command(name='blacklist', description="Blacklists a user from bot usage")
@modcheck()
async def nobotsforu(ctx, mem: disnake.Member, *, reason: str = ""):
    global maybot
    try:
        role = ctx.guild.get_role(1189443616314241034)
        if role:
            chan = maybot.get_channel(1185285161164750992)
            if chan:
                await mem.add_roles(role)
                mes = await ctx.send(f"{mem.mention} has been bot blacklisted!")
                embed = create_embed(description=f"Bot Blacklist | {mem.display_name}", color=disnake.Colour.dark_grey(), fields=[{'name': 'User', 'value': mem.mention}, {'name': 'Moderator', 'value': ctx.author.mention}, {'name': 'Reason', 'value': "No reason provided" if reason == "" else reason}, {'name': 'Message Link', 'value': mes.jump_url}])
                await chan.send(embed=embed)
            else:
                await ctx.send("Channel not found.")
        else:
            await ctx.send("Role not found.")
    except disnake.Forbidden:
        await ctx.send("I don't have permission to do that.")
    print("Blank command")

def setup_command(cog):
# Global Marker
    global maybot
    maybot = cog.bot
    cog.bot.add_command(nobotsforu)
    return nobotsforu