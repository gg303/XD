import random
import discord
import time
import datetime
from discord.ext import commands
from discord import FFmpegAudio
import youtube_dl
from discord.utils import get
#prefix
bot = commands.Bot(command_prefix="!")
from youtube_dl import YoutubeDL
#On_Ready
@bot.event
async def on_ready():
        await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.listening, name="!commands to get help"))
        print("Loged In ")
        bot.remove_command('help')
        channel = bot.get_channel(879641894576091139)
        await channel.send("The Bot Is Online From A Restart/Shutdown")

@bot.command()
async def commands(ctx):
    embed = discord.Embed(title="Commands", description="Here You Can See All The Commands", color=0x00ff00)
    embed.add_field(name="!join", value="The Bot Wil Join The Call", inline=False)
    embed.add_field(name="!leave", value="The Bot Wil Leave The Call", inline=False)
    embed.add_field(name="!say", value="The Bot Wil Say Anything In The Call", inline=False)
    #embed.add_field(name="!ticket_create", value="You Can Create A Ticket And A Admin Will Reply In Your DMs", inline=False)

    await ctx.send(embed=embed)

@bot.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()

    else:
        await ctx.send("Stop Tricking Me Your Not In A Voice Channel :angry:")

@bot.command(pass_context = True)
async def leave(ctx): # Note: ?leave won't work, only ?~ will work unless you change  `name = ["~"]` to `aliases = ["~"]` so both can work.
    if (ctx.voice_client): # If the bot is in a voice channel
        await ctx.guild.voice_client.disconnect() # Leave the channel
        await ctx.send('Bot left')
    else: # But if it isn't
        await ctx.send("I'm not in a voice channel, use the join command to make me join")
@bot.command(pass_context = True)
async def say(ctx, Reason = None):
    if (ctx.author.voice):
        await ctx.send(Reason, tts=True)


@bot.command()
async def ticket_create(ctx):
    await ctx.author.send("Please Enter Your Question By Typing !Q {your question} (instead of spaces please type a _ )")
@bot.command()
async def Q(ctx, Question = None):
    admin = bot.get_user(744925376782008451)
    admin2 = bot.get_user(762213101436796948)
    channel = bot.get_channel(879678632593858610)
    await ctx.author.send("Your Question Has Been Sent. Please Wait For A Response")
    await channel.send(f"Question From {ctx.author} The Question Is {Question}")

@bot.command()
async def who_is(ctx, member = None):
    embed = discord.Embed(title=f"{member.id}", description=" ", color=0x00ff00)
    embed.add_field(name=f"{member.activity}", value=" ", inline=False)
    await ctx.send(embed=embed)

bot.run('ODc5NjUzODk2NzQ0NzMwNjQ0.YSS3iA.1Gp7RrIJzDxDJWd222NHo1m3KIE')
