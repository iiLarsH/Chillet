import asyncio
import discord
import sqlite3
from discord.ext import commands
from discord import app_commands
from ReusedFunctions.ButtonMenu import ButtonMenu
from ReusedFunctions.Emoji import get_emoji, get_foodbar, get_work
from ReusedFunctions.CreateStatPages import create_stat_pages

class PalStats(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("palstats.py is ready")

    @app_commands.command(name="palstats", description="Gives the given pal stats.")
    @app_commands.describe(palname="Name of the pal you want stats from")
    async def palstats(self, interaction: discord.Interaction, palname: str):
        pages = create_stat_pages(palname)
        await interaction.response.send_message(embed=pages[0], view=ButtonMenu(pages, 60, interaction.user))

    @palstats.autocomplete("palname")
    async def autocomplete_palname(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
        data = []
        con = sqlite3.connect("Database/Paldata.db")
        cur = con.cursor()
        palnames = cur.execute("SELECT name FROM pal")
        for palname in palnames.fetchall():
            if current.lower() in palname[0].lower():
                data.append(app_commands.Choice(name=palname[0], value=palname[0]))
        return data[:25]

    @palstats.error
    async def on_command_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        print(error)

async def setup(client):
    await client.add_cog(PalStats(client))
