import os
from discord.ext import commands
from discord import app_commands
import discord
import asyncio

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
    print("Succes: Bot has started working")

async def load():
    for filename in os.listdir("./Commands"):
        if filename.endswith(".py"):
            await client.load_extension(f"Commands.{filename[:-3]}")

@client.command()
async def sync(ctx):
    print("start sync")
    if ctx.message.author.id == 262672220260663297:
        synced = await client.tree.sync()
        print(f'You synced {str(len(synced))} commands')
    else:
        await ctx.send("```You must be the botowner to use this command!```")

@client.tree.error
async def on_app_command_error(interaction, error):
    print(f"{error}")
                                        
async def main():
    async with client:
        await load()
        await client.start("MTIwODA3OTQ1NDI3OTA0NTE5MA.G3Nng2.zpvVbQV4kLTVP9okrsbj3DDXyZDRtXmeRiy9Es")

asyncio.run(main())