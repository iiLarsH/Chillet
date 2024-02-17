import asyncio
import discord
import sqlite3
from discord.ext import commands
from discord import app_commands
from ReusedFunctions.ButtonMenu import ButtonMenu
from ReusedFunctions.Emoji import get_emoji, get_foodbar, get_work

class PalStats(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("palstats.py is ready")

    @app_commands.command(name="palstats", description="Gives the given pal stats.")
    @app_commands.describe(palname="Name of the pal you want stats from")
    async def palstats(self, interaction: discord.Interaction, palname: str):
        con = sqlite3.connect("Database/Paldata.db")
        cur = con.cursor()
        data = cur.execute("SELECT paldecknr, palnr_suffix, name, size, element_1, element_2, hp, range_atk, defense, ai_response, slow_walk_speed, walk_speed, run_speed, ride_sprint_speed, max_stomach, food_amount, nocturnal, stamina, maleprob, breedingpower, igniting, watering, planting, electricity, handiwork, gathering, logging, mining, medicine, cooling, transporting, farming, mount, mounttype FROM pal WHERE name = ?", (palname,))
        paldecknr, palnr_suffix, name, size, ele1, ele2, hp, rangeatk, defense, ai_response, slow_walk_speed, walk_speed, run_speed, ride_sprint_speed, max_stomach, food_amount, nocturnal, stamina, maleprob, breedingpower, igniting, watering, planting, electricity, handiwork, gathering, logging, mining, medicine, cooling, transporting, farming, mount, mounttype = data.fetchone()

        data = cur.execute("SELECT partnerskill, description FROM pal_partner_skills WHERE name = ?", (palname,))
        partnerskill, description = data.fetchone()

        data = cur.execute("SELECT imagelink FROM pal_images WHERE name = ?", (palname,))
        img = data.fetchone()

        if (palnr_suffix == None):
            palnr_suffix = ''

        pages = []
        if(nocturnal == "TRUE"):
            nocturnal = "Night"
        else:
            nocturnal = "Day"

        work_levels = {"Igniting": igniting, "Watering": watering, "Planting": planting, "Gen_Electricity": electricity, "Handiwork": handiwork, "Gathering": gathering, "Logging": logging, "Mining": mining, "Medicine": medicine, "Cooling": cooling, "Transporting": transporting, "Farming": farming}


        GeneralStats = discord.Embed(title="PalStats: Overall", description=f"**PalDeckNr**: {str(paldecknr) + str(palnr_suffix)}\n**Palname**: {name}", colour=discord.Colour.dark_blue())
        GeneralStats.add_field(name="Element 1", value=f"{get_emoji(ele1)}{ele1}", inline=True)
        GeneralStats.add_field(name="Element 2", value=f"{get_emoji(ele2)}{ele2}", inline=True)
        GeneralStats.add_field(name="Size", value=f"{size}", inline=False)
        GeneralStats.add_field(name="Nocturnal", value=f"{get_emoji(nocturnal)}", inline=True)
        GeneralStats.add_field(name="♂️/♀️", value=f"{str(maleprob)}" + "/" + f"{str(100 - maleprob)}", inline=False)
        GeneralStats.add_field(name="Breedingpower", value=f"{breedingpower}", inline=True)
        GeneralStats.set_footer(text="Lower breedingpower is better")
        pages.append(GeneralStats)

        Combat = discord.Embed(title="PalStats: Combat", description=f"**PalDeckNr**: {str(paldecknr) + str(palnr_suffix)}\n**Palname**: {name}", colour=discord.Colour.red())
        Combat.add_field(name="HP", value=f"<:HP:1208242909598720130>{hp}", inline=True)
        Combat.add_field(name="ATK", value=f"<:ATK:1208242876304195715>{rangeatk}", inline=True)
        Combat.add_field(name="DEF", value=f"<:DEF:1208242878934159390>{defense}", inline=False)
        Combat.add_field(name="Wild Pal Response", value=f"{ai_response}", inline=True)
        pages.append(Combat)

        Mount = discord.Embed(title="PalStats: Mount", description=f"**PalDeckNr**: {str(paldecknr) + str(palnr_suffix)}\n**Palname**: {name}", colour=discord.Colour.orange())
        Mount.add_field(name="Mount Enabled", value=f"{get_emoji(mount)}", inline=True)
        Mount.add_field(name="Mount Type", value=f"{get_emoji(mounttype)}", inline=True)
        Mount.add_field(name="Stamina", value=f"{stamina}", inline=False)
        Mount.add_field(name="Slow Walk Speed", value=f"{slow_walk_speed}", inline=True)
        Mount.add_field(name="Walk Speed", value=f"{walk_speed}", inline=True)
        Mount.add_field(name="Run Speed", value=f"{run_speed}", inline=True)
        Mount.add_field(name="Ride Sprint Speed", value=f"{ride_sprint_speed}", inline=True)
        Mount.set_footer(text="Slow walk speed refers to speed while overburdend")
        pages.append(Mount)

        Work = discord.Embed(title="PalStats: Work", description=f"**PalDeckNr**: {str(paldecknr) + str(palnr_suffix)}\n**Palname**: {name}", colour=discord.Colour.teal())
        Work.add_field(name="Max Stomach", value=f"<:MaxFood:1208243345672114176>{max_stomach}", inline=True)
        Work.add_field(name="Food consumption", value=f"{get_foodbar(food_amount)}", inline=True)
        Work.add_field(name="Worktype and level", value=f"{get_work(work_levels)}", inline=False)
        pages.append(Work)

        Partner_skill = discord.Embed(title="PalStats: Partner Skill", description=f"**PalDeckNr**: {str(paldecknr) + str(palnr_suffix)}\n**Palname**: {name}", colour=discord.Colour.dark_purple())
        Partner_skill.add_field(name="Partner skill name", value=f"{partnerskill}", inline=False)
        Partner_skill.add_field(name="Description", value=f"{description}", inline=False)
        pages.append(Partner_skill)

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
