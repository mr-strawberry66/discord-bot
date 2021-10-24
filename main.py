from discord.ext import commands
import discord
import os

ROLE_NAME = os.environ["ROLE_NAME"]
TOKEN = os.environ["TOKEN"]

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print("------")


@bot.event
async def on_member_join(user: discord.Member):
    role = [role for role in user.guild.roles if role.name == ROLE_NAME][0]
    await user.add_roles(role)


bot.run(TOKEN)
