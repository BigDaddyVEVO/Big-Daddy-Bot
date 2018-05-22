import random
import asyncio
import aiohttp
import discord
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands

TOKEN = "NDQ3ODk4MTA5MDc1NTIxNTU3.DeOSPg.HGnCAQ5XTTnmz5qRbdTMB3Ugi-o"  # Get at discordapp.com/developers/applications/me

bot = commands.Bot(description="BigDaddy Bot can do a range of different things, including shagging your mum.",command_prefix=("BD.", "bd."))

@bot.command() #Test to see if bot works.
async def bigdaddy():
  "The bot speaks to you."
  await bot.say("Fuck off.")


@bot.command(pass_context=True)
async def say(ctx, *, something=None):
    if something is None:
        await bot.say("Fucking hurry up and tell me what you want to say you silly little shit.")
    else:
      await bot.say(something)


@bot.command() #Kicks a member
async def kick(member:discord.Member):
    await bot.kick(member)

@bot.command() #Bans a member
async def ban(member:discord.Member):
    await bot.kick(member)

@bot.command()#Unbans a member(Works for hackbans)
async def unban(member:discord.Member):
    await bot.kick(member)

@bot.command() #Hackbans a member
async def hackban(member:discord.Member):
    await bot.kick(member)


##############Games on ur phone##############
@commands.cooldown(rate=1, per=5, type=commands.BucketType.channel)
@bot.command(name='8ball',
                description="Answers a yes/no question.",
                brief="BigDaddy will predict the future for you.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
  possible_responses = [
        'There is a higher chance of you losing your virgnity (A solid no)',
        'The chance of it is happening is almost as small as your penis.',
        'I can not put my finger on it but I think you should fuck off',
        'Guess theres a chance, I would not put all your fucking money on it though.',
        'Hell to the fucking yes, lets high five and do some Xanax bruva!',
    ]
  await bot.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@bot.event
async def on_ready():
    await bot.change_presence(game=Game(name="BigPP"))
    print(bot.user.name + " joined the party")
    
bot.run (TOKEN)
