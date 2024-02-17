import discord
from discord.ext import commands
from discord import app_commands

class Palbox_add(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("palbox_add.py is ready")

    @app_commands.command(name="palbox_add", description="Adds an pal to the palbox of a player")
    async def palbox_add(self, interaction: discord.Interaction, save: str, palname: str, gender: str ,passive1: str = None, passive2: str = None, passive3: str = None, passive4: str = None):
        bot_latency = round(self.client.latency * 1000)
        await interaction.response.send_message(f"pong! {bot_latency}ms.")


async def setup(client):
    await client.add_cog(Palbox_add(client))