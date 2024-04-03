import discord 
import random
import os
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

global locked
locked = False

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def deletememeID(ctx, arg):
    memefile = open("meme.csv","r+")

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def  deletememe(ctx, arg):
    with open("meme.csv", "r") as fp:
        lines = fp.readlines()
    with open("meme.csv", "w") as fp:
        for line in lines:
            if line.strip("\n").split("?")[0] != str(arg.split("?")[0]):
                print(arg.split("?")[0])
                fp.write(line)
            else:
                await ctx.send("deleted meme")

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def lock(ctx):
    global locked
    if locked == False:
        locked = True
        await ctx.send("bot has been locked")
    else:
        locked = False
        await ctx.send("bot has been unlocked")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def  memelist(ctx):
    memefile = open("meme.csv","r")
    count = -1
    for meme in memefile:
        count +=1
        print(count)
        await ctx.send(str(meme))
        await ctx.send(" meme ID: "+str(count))
"""
^  ADMIN COMMANDS  ^
V END USER COMMANDS V
"""
@bot.command(pass_context=True)
async def meme(ctx):
    global locked
    memefile = open("meme.csv","r")
    memelines = []
    if locked == False:
        cnt = 0
        for line in memefile: 
            cnt += 1
            memelines.append(line)
        memeindex = random.randrange(cnt)
        await ctx.send(memelines[memeindex])

@bot.command(pass_context=True)
async def addmeme(ctx, arg):
     memefile = open("meme.csv","a")
     global locked
     if locked == False:
         memefile.write(arg+"\n")

@bot.command()
async def rules(ctx):
   global locked
   if locked == False:
        await ctx.send("**rules for bot usage goes here**")#for negative to fill out
        await ctx.send("by using this bot you except these rules above")

@bot.command()
async def github(ctx):
    global locked
    if locked == False:
        await ctx.send("https://github.com/Negative-light/")

@bot.command()
async def invitelink(ctx):
    global locked
    if locked == False:
        await ctx.send("share link with friends:")
        await ctx.send("https://discord.gg/CD8e5avNtn")
"""
V  RUNTIME  V
"""
if __name__ == '__main__':
    print("Loading Enviroment Variables")
    load_dotenv()
    MODE = os.getenv("MODE")
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    if MODE == "test":
        print("You are in test mode. The bot will not run but this ensures other features work properly")
        print(f"DISCORD TOEKN: {DISCORD_TOKEN}")
    elif MODE == "prod":
        print("Running Discord Bot")
        bot.run(DISCORD_TOKEN)
