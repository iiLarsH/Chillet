import discord, sqlite3
from discord.ext import commands
from discord import app_commands

class PalStats(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("palstats.py is ready")

    @app_commands.command(name="palstats", description="Gives the given pal stats.")
    @app_commands.describe(palname = "Name of the pal you want stats from")
    async def palstats(self, interaction: discord.Interaction, palname : str):
        con = sqlite3.connect("Database/Paldata.db")
        cur = con.cursor()
        data = cur.execute("SELECT paldecknr, palnr_suffix, name, size, element_1, element_2, hp, range_atk, defense, ai_response, slow_walk_speed, walk_speed, run_speed, ride_sprint_speed, max_stomach, food_amount, nocturnal, stamina, maleprob, breedingpower, igniting, watering, planting, electricity, handiwork, gathering, logging, mining, medicine, cooling, transporting, farming, mount, mounttype FROM pal WHERE name = ?", (palname,))
        paldecknr, palnr_suffix, name, size, ele1, ele2, hp, rangeatk, defense, ai_response, slow_walk_speed, walk_speed, run_speed, ride_sprint_speed, max_stomach, food_amount, nocturnal, stamina, maleprob, breedingpower, igniting, watering, planting, electricity, handiwork, gathering, logging, mining, medicine, cooling, transporting, farming, mount, mounttype = data.fetchone()

        data = cur.execute("SELECT partnerskill, description FROM pal_partner_skills WHERE name = ?", (palname,))
        partnerskill, description = data.fetchone()

        data = cur.execute("SELECT imagelink FROM pal_images WHERE name = ?", (palname, ))
        img = data.fetchone()

        if(palnr_suffix == None):
            palnr_suffix = ''
        
        GeneralStats = discord.Embed(title="PalStats: Overall", description=f"**PalDeckNr**: {str(paldecknr) + str(palnr_suffix)}\n**Palname**: {name}", colour=discord.Colour.dark_blue())
        GeneralStats.add_field(name="Element 1", value=f"{ele1}", inline=True)
        GeneralStats.add_field(name="Element 2", value=f"{ele2}", inline=True)
        GeneralStats.add_field(name="Size", value=f"{size}", inline=False)
        GeneralStats.add_field(name="Nocturnal", value=f"{nocturnal}", inline=True)
        GeneralStats.add_field(name="Male/Female", value=f"{str(maleprob)}"+"/"+ f"{str(100-maleprob)}", inline=False)
        GeneralStats.add_field(name="Breedingpower", value=f"{breedingpower}", inline=True)
        

        Combat = discord.Embed(title="PalStats: Combat", description=f"**PalDeckNr**: {str(paldecknr) + str(palnr_suffix)}\n**Palname**: {name}", colour=discord.Colour.red())
        Combat.add_field(name="HP", value=f"{hp}", inline=True)
        Combat.add_field(name="ATK", value=f"{rangeatk}", inline=True)
        Combat.add_field(name="DEF", value=f"{defense}", inline=False)
        Combat.add_field(name="Wild Pal Response", value=f"{ai_response}", inline=True)

        Mount = discord.Embed(title="PalStats: Mount", description=f"**PalDeckNr**: {str(paldecknr) + str(palnr_suffix)}\n**Palname**: {name}", colour=discord.Colour.orange())
        Mount.add_field(name="Mount Enabled", value=f"{mount}", inline=True)
        Mount.add_field(name="Mount Type", value=f"{mounttype}", inline=True)
        Mount.add_field(name="Slow Walk Speed", value=f"{slow_walk_speed}", inline=True)
        Mount.add_field(name="Walk Speed", value=f"{walk_speed}", inline=True)
        Mount.add_field(name="Run Speed", value=f"{run_speed}", inline=True)
        Mount.add_field(name="Ride Sprint Speed", value=f"{ride_sprint_speed}", inline=True)
        Mount.add_field(name="Stamina", value=f"{stamina}", inline=True)

        Work = discord.Embed(title="PalStats: Work", description=f"**PalDeckNr**: {str(paldecknr) + str(palnr_suffix)}\n**Palname**: {name}", colour=discord.Colour.teal())
        Work.add_field(name="Max Stomach", value=f"{max_stomach}", inline=True)
        Work.add_field(name="Food consumption", value=f"{food_amount}", inline=True)
        Work.add_field(name="Worktype and level", value=f"Igniting: {igniting}\n Watering: {watering}\n Planting: {planting}\n Electricity: {electricity}\n Handiwork: {handiwork}\n Gathering: {gathering}\n Logging: {logging}\n Mining: {mining}\n Medicine: {medicine}\n Cooling: {cooling}\n Transporting: {transporting}\n Farming: {farming}", inline=False)

        Partner_skill = discord.Embed(title="PalStats: Partner Skill", description=f"**PalDeckNr**: {str(paldecknr) + str(palnr_suffix)}\n**Palname**: {name}", colour=discord.Colour.dark_purple())
        Partner_skill.add_field(name="Partner skill name", value=f"{partnerskill}", inline=False)
        Partner_skill.add_field(name="Description", value=f"{description}", inline=False)

        await interaction.response.send_message(embed=GeneralStats)

    @palstats.autocomplete("palname")
    async def autocomplete_palname(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
        data = []
        con = sqlite3.connect("Database/Paldata.db")
        cur = con.cursor()
        palnames = cur.execute("SELECT name FROM pal")
        for palname in palnames.fetchall():
            if(current.lower() in palname.lower()):
                data.append(app_commands.Choice(name=palname, value=palname))
        return data[:25]
    
    @palstats.error
    async def on_command_error(self, interaction: discord.Interaction, error : app_commands.AppCommandError):
        print(error)

async def setup(client):
    await client.add_cog(PalStats(client))