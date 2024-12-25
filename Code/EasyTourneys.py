import discord
from discord.ext import commands
import os
import random
import string
import time
import re
import pandas as pd
import openpyxl

# Load the bot token from environment variables
TOKEN = os.environ['TOKEN']

# Configure intents and initialize the bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


# Command: Ping
@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    pingEmbed = discord.Embed(title="Ping? Pong!",
                              description=f"The bot latency is {latency}ms.",
                              color=discord.Color.green())
    await ctx.send(embed=pingEmbed)


# Command: Submit (sends instructions to the user via DM)
@bot.command()
async def submit(ctx):
    try:
        # Send a DM to the user with submission instructions
        submitEmbed = discord.Embed(
            title="Instructions for Submission",
            description=
            "Send the link of your submission here in the form `!link <link>`.",
            color=discord.Color.green())
        await ctx.author.send(embed=submitEmbed)

        # Confirmation message in the channel
        confirmationEmbed = discord.Embed(
            title="DM Sent!",
            description=
            "Check your DMs and follow the instructions to submit your link.",
            color=discord.Color.green())
        await ctx.send(embed=confirmationEmbed)

        # Attempt to delete the user's command message (if the bot has permission)
        if ctx.guild and ctx.channel.permissions_for(
                ctx.guild.me).manage_messages:
            await ctx.message.delete()
    except discord.Forbidden:
        # If the bot cannot send a DM, notify the user in the channel
        errorEmbed = discord.Embed(
            title="DM Failed",
            description=
            "I couldn't send you a DM. Please enable direct messages from server members.",
            color=discord.Color.red())
        instructionsEmbed = discord.Embed(
            title="How to Enable Direct Messages from Server Members?",
            description=(
                "1. Click on the dropdown menu near the server banner.\n"
                "2. Go to 'Privacy Settings'.\n"
                "3. Toggle 'Direct Messages' to ON.\n"
                "4. Run the `!submit` command again."),
            color=discord.Color.blue())
        await ctx.send(embed=errorEmbed)
        await ctx.send(embed=instructionsEmbed)


# Command: Link (handles submission links and validates them)
@bot.command()
async def link(ctx, *, link: str):
    # Check if the message is a DM
    if not isinstance(ctx.channel, discord.DMChannel):
        dmOnlyEmbed = discord.Embed(
            title="Command Restricted",
            description=
            "Please use this command in a direct message to the bot.",
            color=discord.Color.red())
        await ctx.send(embed=dmOnlyEmbed)
        return

    # Validate the link using a regular expression
    urlPattern = re.compile(
        r'^(http|https)://[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(/.*)?$')
    if not urlPattern.match(link):
        invalidLinkEmbed = discord.Embed(
            title="Invalid Link",
            description=
            "The link you provided is invalid. Please enter a valid URL using `!link <link>`.",
            color=discord.Color.red())
        await ctx.send(embed=invalidLinkEmbed)
        return

    # Generate a unique identifier
    alpha = "".join(random.choices(string.ascii_uppercase, k=3))
    unixTime = int(time.time())
    digits = str(unixTime)[-5:]
    uniqueID = alpha + digits

    userID = ctx.author.id

    # Save the link and unique ID to the file
    try:
        with open("links.txt", "a") as file:
            file.write(f"{link} | {uniqueID} | {userID}\n")

        submittedEmbed = discord.Embed(
            title="Submission Approved!",
            description=
            f"Your submission has been saved and approved.\nUnique Code: {uniqueID}",
            color=discord.Color.green())
        await ctx.send(embed=submittedEmbed)
    except Exception as e:
        errorSavingEmbed = discord.Embed(
            title="Error Occurred",
            description=f"An error occurred while saving your submission: {e}",
            color=discord.Color.red())
        await ctx.send(embed=errorSavingEmbed)


# Command: Checkuser (retrieves the user who made a submission)
@bot.command()
async def checkuser(ctx, identifier: str):
    try:
        with open("links.txt", "r") as file:
            for line in file:
                parts = line.strip().split(" | ")
                if parts[1] == identifier:
                    link = parts[0]
                    userID = int(parts[2])
                    user = await bot.fetch_user(userID)
                    submissionEmbed = discord.Embed(
                        title="Submission Found",
                        description=
                        f"The submission is by {user.mention}.\nLink: {link}",
                        color=discord.Color.green())
                    await ctx.send(embed=submissionEmbed)
                    return
        notFoundEmbed = discord.Embed(
            title="Submission Not Found",
            description="No submission found with the given identifier.",
            color=discord.Color.red())
        await ctx.send(embed=notFoundEmbed)
    except Exception as e:
        errorEmbed = discord.Embed(title="Error Occurred",
                                   description=f"An error occurred: {e}",
                                   color=discord.Color.red())
        await ctx.send(embed=errorEmbed)


# Command: Export (exports the data to an Excel file)
@bot.command()
async def export(ctx):
    try:
        # Read data from the links.txt file
        data = []
        with open("links.txt", "r") as file:
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) == 3:
                    url, identifier, userID = parts
                    data.append([url, identifier, userID])

        # Create a DataFrame and save to an Excel file
        df = pd.DataFrame(data, columns=["URL", "Identifier", "UserID"])
        excelFilename = "exported_data.xlsx"
        df.to_excel(excelFilename, index=False)

        # Send the Excel file in the Discord chat
        with open(excelFilename, "rb") as file:
            fileEmbed = discord.Embed(
                title="Exported Data",
                description="Here is the exported data in an Excel file.",
                color=discord.Color.green())
            await ctx.send(embed=fileEmbed,
                           file=discord.File(file, excelFilename))
    except Exception as e:
        errorEmbed = discord.Embed(title="Error Occurred",
                                   description=f"An error occurred: {e}",
                                   color=discord.Color.red())
        await ctx.send(embed=errorEmbed)


# Run the bot
bot.run(TOKEN)
