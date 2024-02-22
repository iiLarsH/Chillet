import discord
from discord.ext import commands
from discord import app_commands
import sqlite3
from ReusedFunctions.ButtonMenu import ButtonMenu
from ReusedFunctions.GetAllPals import get_all_pals
from ReusedFunctions.CreateDesiredChildPages import DividePages

class Get_Desired_Child(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Get_Desired_Child.py is ready")

    @app_commands.command(name="get_desired_child", description="Gives all combonations to make a pal, with a given parent or without")
    async def get_desired_child(self, interaction: discord.Interaction, desired_child: str, required_parent: str = ""):
        con = sqlite3.connect("Database/Paldata.db")
        cur = con.cursor()
        if required_parent == "":
            required_parent = '%'

        query = """
                SELECT parent1, parent2, child
                FROM (
                    SELECT parent1, parent2, child,
                        CASE WHEN parent1 <= parent2 THEN parent1 || ',' || parent2 ELSE parent2 || ',' || parent1 END AS parent_combo
                    FROM all_combo_pal_breeding
                ) AS subquery
                WHERE child = ? AND (parent1 LIKE ? OR parent2 LIKE ?)
                GROUP BY child, parent_combo
                """
        all_combo = cur.execute(query, (desired_child, required_parent, required_parent))
        combo_list = []

        for i in all_combo:
            combo = str(i[0] + " + " + i[1] + " = " + i[2])
            combo_list.append(combo)

        pages = DividePages(combo_list)

        await interaction.response.send_message(embed=pages[0], view=ButtonMenu(pages, 60, interaction.user))

    @get_desired_child.autocomplete("desired_child")
    async def autocomplete_desired_child(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
        data = []
        palnames = get_all_pals()
        for palname in palnames.fetchall():
            if current.lower() in palname[0].lower():
                data.append(app_commands.Choice(name=palname[0], value=palname[0]))
        return data[:25]
    
    @get_desired_child.autocomplete("required_parent")
    async def autocomplete_required_parent(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
        data = []
        palnames = get_all_pals()
        for palname in palnames.fetchall():
            if current.lower() in palname[0].lower():
                data.append(app_commands.Choice(name=palname[0], value=palname[0]))
        return data[:25]

async def setup(client):
    await client.add_cog(Get_Desired_Child(client))