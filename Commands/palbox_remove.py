import discord
from discord.ext import commands
from discord import app_commands

class Palbox_remove(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("palbox_remove.py is ready")

    @app_commands.command(name="palbox_remove", description="Gives the bot latency in ms.")
    async def slashping(self, interaction: discord.Interaction):
        bot_latency = round(self.client.latency * 1000)
        await interaction.response.send_message(f"pong! {bot_latency}ms.")


async def setup(client):
    await client.add_cog(Palbox_remove(client))