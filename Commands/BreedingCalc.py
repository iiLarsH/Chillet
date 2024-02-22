from types import NoneType
import discord, sqlite3
from discord.ext import commands
from discord import app_commands
from ReusedFunctions.ButtonMenu import ButtonMenu
from ReusedFunctions.CreateStatPages import create_stat_pages
from ReusedFunctions.GetAllPals import get_all_pals

class BreedingCalc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("BreedingCalc.py is ready")

    @app_commands.command(name="breeding_calc", description="Uses 2 parents to calculate the child.")
    async def breeding_calc(self, interaction: discord.Interaction, parent1: str, parent2: str):
        con = sqlite3.connect("Database/Paldata.db")
        cur = con.cursor()

        data_child = cur.execute("SELECT child FROM all_combo_pal_breeding WHERE parent1 = ? and parent2 = ?", (parent1, parent2,))
        name_child = data_child.fetchone()
        name_child = name_child[0]

        data_parent1 = cur.execute("SELECT paldecknr, palnr_suffix, name FROM pal WHERE name = ?", (parent1,))        
        paldecknr1, palnr_suffix1, name1 = data_parent1.fetchone()

        data_parent2 = cur.execute("SELECT paldecknr, palnr_suffix, name FROM pal WHERE name = ?", (parent2,))
        paldecknr2, palnr_suffix2, name2 = data_parent2.fetchone()

        data_child = cur.execute("Select paldecknr, palnr_suffix, name FROM pal WHERE name = ?", (name_child,))
        paldecknr_child, palnr_suffix_child, name_child = data_child.fetchone()

        data = cur.execute("SELECT imagelink FROM pal_images WHERE name = ?", (name_child,))
        img = data.fetchone()
        con.close()

        if (palnr_suffix1 is None):
            palnr_suffix1 = ''  

        if (palnr_suffix2 is None):
            palnr_suffix2 = ''

        if (palnr_suffix_child is None):
            palnr_suffix_child = ''

        pages = []
        Breedpage = discord.Embed(title="Outcome Breed")
        Breedpage.add_field(name="Parents", value=f"**Name parent 1**: {name1}\n**Paldecknr parent 1**: {str(paldecknr1)+str(palnr_suffix1)}\n**Name parent 2**: {name2}\n**Paldecknr parent 2**:{str(paldecknr2)+str(palnr_suffix2)}", inline=False)
        Breedpage.add_field(name="Child:", value=f"**Paldecknr child**:\t{str(paldecknr_child)+str(palnr_suffix_child)}\n**Childname**:\t{name_child}", inline=False)
        Breedpage.set_image(url=f"{img[0]}")
        pages.append(Breedpage)

        extrapages = create_stat_pages(name_child)

        pages.extend(extrapages)
        
        await interaction.response.send_message(embed=pages[0], view=ButtonMenu(pages, 60, interaction.user))

    @breeding_calc.autocomplete("parent1")
    async def autocomplete_parent1(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
        data = []
        palnames = get_all_pals()
        for palname in palnames.fetchall():
            if current.lower() in palname[0].lower():
                data.append(app_commands.Choice(name=palname[0], value=palname[0]))
        return data[:25]
    
    @breeding_calc.autocomplete("parent2")
    async def autocomplete_parent2(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
        data = []
        palnames = get_all_pals()
        for palname in palnames.fetchall():
            if current.lower() in palname[0].lower():
                data.append(app_commands.Choice(name=palname[0], value=palname[0]))
        return data[:25]

    @breeding_calc.error
    async def on_command_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        print(error)


async def setup(client):
    await client.add_cog(BreedingCalc(client))