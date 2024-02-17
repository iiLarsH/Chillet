import discord
from discord.ext import commands
from discord import app_commands

class get_palbox(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("get_palbox.py is ready")

    @app_commands.command(name="get_palbox", description="Gets the palbox from a certain save")
    async def get_palbox(self, interaction: discord.Interaction, save: str):
        await interaction.response.send_message(f"```{save}```")


async def setup(client):
    await client.add_cog(get_palbox(client))