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
#import tts
web = read_web()
memelist = []
#memelist = ["https://cdn.discordapp.com/attachments/982758636021489697/1091087876181213304/Li50rO4.webp","https://cdn.discordapp.com/attachments/982758636021489697/1091087876604833912/a8fxblo2alna1.png","https://cdn.discordapp.com/attachments/982758636021489697/1091087877062017166/IMG_1198.png.jpg","https://cdn.discordapp.com/attachments/982758636021489697/1091087877326254171/orange-with-blue-peel.png","https://cdn.discordapp.com/attachments/982758636021489697/1091087877661790288/programmers-who-unit-test-their-code-only-with-their-eyes-and-find-runtime-issues-yuvakrishnamemes.jpg","https://cdn.discordapp.com/attachments/982758636021489697/1091087877884100628/pnfgniehefna1.png","https://cdn.discordapp.com/attachments/982758636021489697/1091087878228029600/tumblr_d7a4a2fa84c6cb03783f5f3de4f73c4f_c72a920f_400.png","https://cdn.discordapp.com/attachments/982758636021489697/1091087878479679488/Screenshot_20230310-092404-537.png","https://cdn.discordapp.com/attachments/982758636021489697/1091087220947026000/image-25.png","https://cdn.discordapp.com/attachments/982758636021489697/1091087221597159454/h5805D173.jpg","https://cdn.discordapp.com/attachments/982758636021489697/1091087221832044704/finally-found-my-spirit-animal-33-glonk-glonk-does-absolutely-nothing-and-dies-ig-pakalupapitocamel.jpg","https://cdn.discordapp.com/attachments/982758636021489697/1091087222314369244/well-can-comprehend-these-manmade-horrors-perfectly-fine-so-idk-maybe-have-skill-issue-or-smth.png","https://cdn.discordapp.com/attachments/982758636021489697/1091087222545076354/shadow-people-always-lurk-their-peripheral-vision-and-they-are-never-really-sure-if-they-are-alone.jpg","https://cdn.discordapp.com/attachments/982758636021489697/1091087222763175946/hat-find-man-who-can-do-all-three-poet-philosors-failure-pher.jpg","https://cdn.discordapp.com/attachments/982758636021489697/1091087222092087366/dog-wondered-why-my-dog-wouldnt-come-called-him-then-found-this.jpg","https://cdn.discordapp.com/attachments/982758636021489697/1091087875887599648/IMG_7688.jpg","https://cdn.discordapp.com/attachments/982758636021489697/1091087221320339486/helmet-make-first-contact-with-aliens-yall-got-any-space-memes.jpg","https://cdn.discordapp.com/attachments/982758636021489697/1091086146777395281/v4o5rmy0h4h91.webp","https://cdn.discordapp.com/attachments/982758636021489697/1091086147104542740/tumblr_488ce3975e72edecdcaa963bdfb7ef97_ddb09d22_1280.png","https://cdn.discordapp.com/attachments/982758636021489697/1091086147389767730/CE7FCA49-C9D5-4DB0-8BC4-FF231F7E8788.jpg","https://cdn.discordapp.com/attachments/982758636021489697/1091086147104542740/tumblr_488ce3975e72edecdcaa963bdfb7ef97_ddb09d22_1280.png","https://cdn.discordapp.com/attachments/982758636021489697/1091086921272393728/image0-42.png","https://cdn.discordapp.com/attachments/982758636021489697/1091086921519874078/pixil-gif-drawing_3.gif","https://cdn.discordapp.com/attachments/982758636021489697/1091086921930907778/tem.webp","https://cdn.discordapp.com/attachments/982758636021489697/1091086922358734940/1667090227582.jpg","https://cdn.discordapp.com/attachments/982758636021489697/1091086922891403334/Screenshot_20230317-2116072.png","https://cdn.discordapp.com/attachments/982758636021489697/1091086923428278302/Screenshot_20230317-155830-088.png","https://cdn.discordapp.com/attachments/982758636021489697/1091085794090946651/Screenshot_20220606-200956_Reddit.jpg","https://cdn.discordapp.com/attachments/982758636021489697/1091085794724286505/x2-dont-waste-time-on-phone-simply-stare-blankly-into-space-instead-wiki-have-witty-conversation.jpg","https://cdn.discordapp.com/attachments/982758636021489697/1091085795055652974/share-zo-too-fancy-weed-store-cops-if-quick-friend-ships-if-sucks-hit-da-bricks-real-winners-quit.jpg","https://cdn.discordapp.com/attachments/982758636021489697/1091086146425077760/Screenshot_20230327-210305-144.png","https://cdn.discordapp.com/attachments/982758636021489697/1091085794090946651/Screenshot_20220606-200956_Reddit.jpg","https://cdn.discordapp.com/attachments/935989994735169546/1090977393847582810/13C23846-91A1-432F-BE09-FBB308C495E6.png","https://cdn.discordapp.com/attachments/935989994735169546/1090977710928564374/received_249170060787848.png","https://cdn.discordapp.com/attachments/935989994735169546/1090978517811990558/338200000_1596106454147254_219994394856534837_n_1.png","https://cdn.discordapp.com/attachments/935989994735169546/1090978567199932466/Fq38u-xacAEkeZ6.png","https://cdn.discordapp.com/attachments/935989994735169546/1090978266384453774/20230330_143736.png","https://cdn.discordapp.com/attachments/935989994735169546/1090977294912323624/IMG_0596.jpg","https://cdn.discordapp.com/attachments/454962031607414784/1086460970177658940/CE6AC671-0C9D-40F9-8EC0-7AC67B4298FA.png","https://cdn.discordapp.com/attachments/454962031607414784/1086286499949056040/Screenshot_20230314-072451-975.png","https://cdn.discordapp.com/attachments/454962031607414784/1087633834532687983/Screenshot_20230320-225405-890.png","https://cdn.discordapp.com/attachments/454962031607414784/1090039638477000705/1D666A7E-35E6-4FD2-B021-9378312E904C.jpg","https://cdn.discordapp.com/attachments/454962031607414784/1090040602810400848/IMG_7274.jpg","https://cdn.discordapp.com/attachments/454962031607414784/1090241574484586606/image-13.png","https://cdn.discordapp.com/attachments/454962031607414784/1090390134110814268/20230328_193451.png","https://cdn.discordapp.com/attachments/454962031607414784/1090581652901744721/Untitled42_20230329122129.png","https://cdn.discordapp.com/attachments/935989994735169546/1090685906274496675/j5ldad04lor81.webp","https://cdn.discordapp.com/attachments/935989994735169546/1090685940617445395/k2seygrdpwpa1.png","https://cdn.discordapp.com/attachments/935989994735169546/1090686387151446026/3C21E64A-2292-4AA0-A37F-413AC2203C70.png","https://cdn.discordapp.com/attachments/717498714259980378/1090266128883912774/IMG_20220730_163242.jpg","https://cdn.discordapp.com/attachments/259741273118867466/1090544334564229210/IMG_2287.png","https://cdn.discordapp.com/attachments/935989994735169546/1090715915982745640/1cf04643fefbbce84a4ab7cca6ee7b08727581031d095bd635656ab931317573_1.mp4","https://cdn.discordapp.com/attachments/935989994735169546/1090716248922402917/image-29-1.png","https://cdn.discordapp.com/attachments/935989994735169546/1090716366304182322/ahhhh.mp4","https://cdn.discordapp.com/attachments/935989994735169546/1090716571686666250/UgsSiPDE9Qj1032T.mp4","https://cdn.discordapp.com/attachments/935989994735169546/1090717792577273946/2Q.jpg","https://cdn.discordapp.com/attachments/935989994735169546/1090717903537569923/Screenshot_2022-12-19-23-32-53-77_572064f74bd5f9fa804b05334aa4f912.jpg","https://cdn.discordapp.com/attachments/935989994735169546/1090718653684646018/0hvJp1MvIjwg0-t_.mp4"]
global blacklistwords
blacklistwords = ["fuck","shit","sex","commie","bitch","nigger","rape","cunt","porn","cum"]#use command or add things manuelly
global nerds
nerds = []
global devs

global locked
locked = ["false"] # the locked bool is a list bc for some unknown reason u can't make a global bool or string
#devs =["crazysmile11012#8990","2k#6272"]
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
        await ctx.send(str(random.choice(memelist)))
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
                    await ctx.send('@mod blacklisted word detected in !addmeme usage')
                    await ctx.send('blacklisted word:')
                    await ctx.send(str(blacklistwords[i]))
                    good = False
                    break
            except:
                memelist.append(arg)
                await ctx.send('nice meme:')
                await ctx.send(arg)
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
@commands.cooldown(1, 30, commands.BucketType.user)
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

bot.run('Token here!')

    
