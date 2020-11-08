import random
from random import choice
import os
import discord
from discord.ext import commands, tasks
import praw
import asyncio
import urllib
import re

reddit = praw.Reddit(
                    client_id = "RMA7WaBStJHxPw",
                    client_secret = "DqBHsZd4037AlTzza-MbiOXqxfQ",
                    username = "MeinWohHoin",
                    password = "#coldmess2",
                    user_agent = "lmaoxdxd"
)
TOKEN = ""

client=commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(status= discord.Status.online, activity= discord.Game('MANNU KA KOTHA | .helpME'))
    print('Bot is ready!')

@client.command(ctx = True)
async def hello(ctx):
    reply =['Hello, sunshine!',
'Howdy, partner!',
'Hey, howdy, hi!',
'What’s kickin’, little chicken?',
'Peek-a-boo!',
'Howdy-doody!',
'Hey there, freshman!',
'Hi, sissy!',
'I come in peace!',
'Put that cookie down!',
'Ahoy, matey!',
'Hiya!',
'Ello, mate.',
'Heeey, baaaaaby.',
'Hi, honeybunch!',
'Oh, yoooouhoooo!',
'How you doin?',
'I like your face.',
"What's cookin', good lookin'?",
"Howdy, miss.",
"Why, hello there!",
"Hey, boo.",
"Hello, pony boy!",
"If only i had a pp"
]
    await ctx.send(random.choice(reply))

@client.command(ctx = True)
async def meme(ctx, subred = ['wamps', 'indianpeoplefacebook', 'IndianMeyMeys', 'IndianDankMemes', 'cursedcomments', 'surrealmemes']):
    theSUB = random.choice(subred)
    subreddit = reddit.subreddit(theSUB)
    all_subs = []
    top = subreddit.top(limit = 100)
    for submission in top:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(title = name)
    em.set_image(url = url)
    em.set_footer(text = f'from r/{theSUB}')
    await ctx.send(embed = em)

@client.command(ctx = True)
#@commands.has_permissions(kick_members = True)   YOU CAN USE THIS TO MAKE IT AN ONLY ADMIN TASK
async def helpME(ctx):
    embed = discord.Embed(title = "HELP MENU", discription = "[.COMMANDS]", colour = discord.Colour.green())
    embed.add_field(name = '1) Say .hello ', value= 'for quick interaction')
    embed.add_field(name = '2) Type .8ball', value ='for YES/NO questions')
    embed.add_field(name = '3) Type .clear <number>', value= 'to stack remove messages')
    embed.add_field(name = '4) Type .meme <subreddit>', value = 'to enjoy random all time top memes')
    embed.add_field(name = '5) Type .whois <@member>', value = 'to know member ID')
    embed.set_footer(text = 'type ".helpMUSIC" for help with music commands')
    await ctx.send(embed = embed)

@client.command(ctx = True)
async def helpMUSIC(ctx):
    embed = discord.Embed(title = "MUSIC COMMANDS HAVE BEEN DISABLED!", discription = "[.COMMANDS]", colour = discord.Colour.blurple())
    #embed.add_field(name = '1) Type .join', value = 'This command makes the bot join the voice channel', inline = True)
    #embed.add_field(name = '2) Type .add', value = 'This command adds a song to the queue', inline = True)
    #embed.add_field(name = '3) Type .play', value = 'This command plays songs', inline = True)
    #embed.add_field(name = '4) Type .remove', value = 'This command removes a song from the queue', inline = True)
    #embed.add_field(name = '5) Type .pause', value = 'This command pauses the song', inline = True)
    #embed.add_field(name = '6) Type .resume', value = 'This command resumes the song', inline = True)
    #embed.add_field(name = '7) Type .view', value = 'This command for looking at the last song added to queue', inline = True)
    #embed.add_field(name = '8) Type .leave', value = 'This command for the bot to leave voice channel', inline = True)
    await ctx.send(embed =embed)

@client.command(ctx = True)
async def clear (ctx, amount=1):
    await ctx.channel.purge(limit = amount + 1)

@client.command(ctx = True, aliases= ['user', 'info'])
async def whois(ctx, member: discord.Member):
    embed = discord.Embed(title = member.name, discription = member.mention, colour = discord.Colour.red())
    embed.add_field(name = 'MemberID', value = member.id, inline= True)
    embed.set_thumbnail( url = member.avatar_url)
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.send(embed =embed)

@client.command(ctx = True, aliases = ['8ball'])
async def _8ball (ctx, *,question):
    
    answers = ["As I see it, yes.",
     "Ask again later.",
     "Better not tell you now.",
     "Cannot predict now.",
     "Concentrate and ask again.",
     "Don’t count on it.",
     "It is certain.",
     "It is decidedly so.",
     "Most likely.",
     "My reply is no.",
     "My sources say no.",
     "Outlook not so good.",
     "Outlook good.",
     "Reply hazy, try again.",
     "Signs point to yes.",
     "Very doubtful.",
     "Without a doubt.",
     "Yes.",
     "Yes – definitely.",
     "You may rely on it."]
    await ctx.send(random.choice(answers))


client.run(TOKEN)