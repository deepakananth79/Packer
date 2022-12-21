import discord
import random
import art
from discord import Spotify
from discord.ext import commands
from datetime import *
from keys import *

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix = "p!", intents = intents, case_insensitive = True)

#When Bot Starts Up
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Rizz Simulator'))
    art.tprint(bot.user.name)
    #await bot.change_presence(status = discord.Status.online, activity = discord.Activity(type = discord.ActivityType.watching, name = "this Server"))
    print('Packing')
    print('---------------------')

#On Member Join
@bot.event
async def on_member_join(ctx, member):
    channel = bot.get_channel(1019857851147104258)
    await channel.send(f'Welcome to the server <@{member.id}>')

#Error Handler
@bot.event
async def on_command_error(ctx, error):
  await ctx.send(f"```{error}```")

#Hello Command
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi {ctx.author.mention}')

#Ping Command
@bot.command()
async def ping(ctx):
    embed = discord.Embed(title = "🏓 Pong!", color = 0x9c7a61, timestamp = datetime.utcnow())
    embed.add_field(name = "Latency", value = f"`{round(bot.latency * 1000)}`ms", inline = True)
    await ctx.send(embed = embed)

#Addition Command
@bot.command()
async def add(ctx, left: float, right: float):
    await ctx.send(f'{left + right}')

#Subtract Command
@bot.command()
async def subtract(ctx, left: float, right: float):
    await ctx.send(f'{left - right}')

#Multiply Command
@bot.command()
async def multiply(ctx, left: float, right: float):
    await ctx.send(f'{left * right}')

#Divide Command
@bot.command()
async def divide(ctx, left: float, right: float):
    await ctx.send(f'{left / right}')

#8ball Command
@bot.command(aliases = ["8ball"])
async def predict(ctx, *, question):
  responses = ["Yes", "Maybe", "No"]
  response = random.choice(responses)
  await ctx.send(f":8ball: {response}")
  print("[COMMAND] Predict")

# color command
@bot.command()
async def color(ctx, hexCode: discord.Color):
  embed = discord.Embed(title = ":trackball: Color Search", description = str(hexCode).lower(), color = hexCode, timestamp = datetime.datetime.utcnow())
  embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
  embed.set_image(url = f"https://www.colorhexa.com/{str(hexCode).lower()[1:]}.png")
  await ctx.send(embed = embed)

# direct message command
@bot.command()
async def dm(ctx, member: discord.Member, *, message):
  if(ctx.author.id == 652307034821361676):
    await member.send(message)
    await ctx.send("✅ Sent!")
  else:
    await ctx.send("❌ Only Dpac can use this command")

#Spotify Command
@bot.command(aliases = ["music", "song"])
async def spotify(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
        pass
    if user.activities:
        for activity in user.activities:
            if isinstance(activity, Spotify):
                embed = discord.Embed(
                    title = f"{user.name}'s Spotify",
                    description = "Listening to {}".format(activity.title),
                    color = 0xC902FF)
                embed.add_field(name="Artist", value=activity.artist)
                embed.add_field(name="Album", value=activity.album)
                embed.set_image(url = activity.album_cover_url)
                embed.set_footer(text = f"Requested by {ctx.author}")
                await ctx.send(embed=embed)


    


bot.run(BOT_TOKEN)