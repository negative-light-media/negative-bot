from freebible import read_web
from freebible import bibles
import random
import time
import datetime
from random import Random
import discord
from discord.ext import commands
import typing

global memelist

web = read_web()
memelist = []
global blacklistwords
blacklistwords = ["fuck","shit","sex","commie","bitch","nigger","rape","cunt","porn","cum"] #use command or add things manuelly

global nerds
nerds = []

global devs
global locked

locked = ["false"] # the locked bool is a list bc for some unknown reason u can't make a global bool or string
devs = []
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

#meme read
print('reading file')
f = open("memes.txt","r")
data = f.read()
#data_into_list = data.replace('\n', ' ').split(",")
data_into_list = data.split("\n")
memelist=data_into_list
print(memelist)
f.close()

#nerdread
print('reading file')
f = open("nerd.txt","r")
data = f.read()
#data_into_list = data.replace('\n', ' ').split(",")
data_into_list = data.split("\n")
nerds=data_into_list
print(nerds)

#devread
print('reading file')
f = open("devs.txt","r")
data = f.read()
#data_into_list = data.replace('\n', ' ').split(",")
data_into_list = data.split("\n")
devs=data_into_list
print(devs)

f.close()
f.close()


@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def test(ctx):
    await ctx.send('dev only')


@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def meme(ctx):
    if locked[0] == "false":
        postit= True
        memetosend = str(random.choice(memelist))
        with open('blockedmemes.txt') as f:
            if memetosend in f.read():
                print("attempted displaying a blocked meme")
                postit = False
        if postit == True:
            await ctx.send(memetosend)


@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def addmeme(ctx, arg):
    if locked[0] == "false":
        i = 0
        good = True
        while good == True:
            try:
                i = i+1
                print(i)
                if str(blacklistwords[i]) in arg.lower():
                    await ctx.send('@Moderator  blacklisted word detected in !addmeme usage')
                    await ctx.send('blacklisted word:')
                    await ctx.send(str(blacklistwords[i]))
                    good = False
                    break
            except:
                postit = True
                with open('blockedmemes.txt') as f:
                    if arg in f.read():
                        print("attempted displaying a blocked meme")
                        postit = False
                if postit == True:
                    memelist.append(arg)
                    await ctx.send(str('nice meme you got there, ',ctx.message.author))
                    await ctx.send('adding to my cringe collection!')
                    break
                    
                    
@bot.command()
@commands.is_owner()
async def printall(ctx):
    i = 0
    while len(memelist) >= i:
        i = i+1
        await ctx.send(str(memelist[i]))
        await ctx.send("meme #:{}".format(i))


@bot.command()
@commands.is_owner()
async def addblacklistword(ctx, arg):
    blacklistwords.append(arg)
    await ctx.send('added word to blacklist')


@bot.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def joinnerds(ctx):
    if locked[0] == "false":
        if str(ctx.message.author) in nerds:
            await ctx.send("{} is a member!!!".format(ctx.message.author.mention))
        else:
            await ctx.send("indoctrinating {} into our ranks".format(ctx.message.author.mention))
            await ctx.send("nerdcult grows!!!")
            nerds.append(str(ctx.message.author))


@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def listnerds(ctx):
    if locked[0] == "false":
        await ctx.send(str(nerds))
        if len(nerds) > 20:
            await ctx.send("Nerds are big now! and deserve a role!!! @everyone")
            await ctx.send("nerds ftw!!!")


@bot.command()
@commands.cooldown(1, 255, commands.BucketType.user)
async def website(ctx):
    if locked[0] == "false":
        await ctx.send("https://www.negative-light.com")


@bot.command(pass_context=True)
@commands.cooldown(1,255, commands.BucketType.user)
async def joincommunityproject(ctx):
    if locked[0] == "false":
        if str(ctx.message.author) in devs:
            await ctx.send("{} is a member!!!".format(ctx.message.author.mention))
        else:
            await ctx.send("adding {} to the list of community devs".format(ctx.message.author.mention))
            devs.append(str(ctx.message.author))


@bot.command(Brief='lists community devs',Description='prints out a list of all registered community developers.')
@commands.cooldown(1, 30, commands.BucketType.user)
async def listdevs(ctx):
    if locked[0] == "false":
        await ctx.send(str(devs))


@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def invitelink(ctx):
    if locked[0] == "false":
        await ctx.send("share link with friends:")
        await ctx.send("https://discord.gg/CD8e5avNtn")


@bot.command()
async def github(ctx):
    if locked[0] == "false":
        await ctx.send("https://github.com/Negative-light/")


@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def donate(ctx):
    if locked[0] == "false":
        await ctx.send("https://ko-fi.com/negative_light")


@bot.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def report(ctx, *args):
    if locked[0] == "false":
        await ctx.send("{} reported violation of #rules".format(ctx.message.author.mention))
        response = ""

        for arg in args:
            response = response + " " + arg
        await ctx.send("violating content: {}".format(response))
        await ctx.send("staff and mods will look into this violation")
        await ctx.send(datetime.datetime.now())


@bot.command()
@commands.is_owner()
async def savefiles(ctx):
    f = open("memes.txt","w")
    memelist1 = str(memelist).replace('[','')
    memelist2 = memelist1.replace(']','')
    memelist3 = memelist2.replace(',','\n')
    memelist4 = memelist3.replace("'",'')
    f.write(memelist4)
    print("memes:",memelist4)
    f.close()

    f = open("nerd.txt","w")
    nerdlists = str(nerds).replace('[','')
    nerdlists2 = nerdlists.replace(']','')
    nerdlists3 = nerdlists2.replace(',','\n')
    nerdlists4 = nerdlists3.replace("'",'')
    f.write(nerdlists4)
    print("nerds:",nerdlists4)
    f.close()

    f = open("devs.txt","w")
    devlists = str(devs).replace('[','')
    devlists2 = devlists.replace(']','')
    devlists3 = devlists2.replace(',','\n')
    devlists4 = devlists3.replace("'",'')
    f.write(devlists4)
    print("devs:",devlists4)
    f.close()

    await ctx.send("wrote {} memes to memes.txt".format(len(memelist)))
    await ctx.send("wrote {} devs to devs.txt".format(len(devs)))
    await ctx.send("wrote {} nerds to nerd.txt".format(len(nerds)))


@bot.command()
async def bible(ctx, *args):
    if locked[0] == "false":
        await ctx.send(str(bibles.web.quote(args[0], args[1], args[2])))


@bot.command()
async def bibleusage(ctx):
    if locked[0] == "false":
        await ctx.send("Search gods holy word from [!bible Book Chapter Verse]")


@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def rules(ctx):
    if locked[0] == "false":
        await ctx.send("**rules for bot usage goes here**")#for negative to fill out
        await ctx.send("by using this bot you except these rules above")


@bot.command()
@commands.is_owner()
async def lockbot(ctx):
    if locked[0] == "true":
        await ctx.send("bot is allready locked")
    else:
        locked[0] = "true"
        await ctx.send("Bot is now on lockdown")


@bot.command()
@commands.is_owner()
async def unlockbot(ctx):
    if locked[0] == "false":
        await ctx.send("bot is allready unlocked")
    else:
        locked[0] = "false"
        await ctx.send("restrictions have been lifted")
        await ctx.send("don't hesatate to use this tool!")

@bot.command()
@commands.is_owner()
async def blockmeme(ctx, arg):
    with open("memes.txt","rw")as f:
        for line in f:
            if arg in line:
                line = line.replace(arg, "")
                print("deleted meme:", arg)
                await ctx.send(str("deleted meme:",arg))
    f.close()
    blockedmemes = open("blockedmemes.txt","rw")
    blockedmemes.write(str(arg))
    blockedmemes.close()
    

token = open("token.env",'r')

bot.run(token.read())

    
