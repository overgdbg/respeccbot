import discord
from discord.ext import commands

TOKEN = 'NDk2MTQwNTcyNDQ1MjQ1NDY1.DpMSvg.pgddjEIT3QdIM4Pt5SQo1YghF-o'

counterf = 0

countert = 0

counterdf = 0

version = 1

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name = '!commands'))
    print ("Loaded up.")

@client.command(pass_context = True)
async def f(ctx, *args):
    global counterf
    thing = ''
    author = ctx.message.author.mention
    for arg in args:
        thing = thing + arg + ' '
    thing = thing[:-1]
    if thing == '':
        await client.say(author + ' has paid their respects.')
        counterf += 1
    elif thing == '@everyone' or thing == '@here':
        await client.say('Fuck off')
    else:
        await client.say(author + ' has paid their respects to ' + thing + ".")
        counterf += 1
    if counterf == 1 and thing != '@everyone' and thing != '@here':
        await client.say('Wow! You are the first to pay respects since bot has started.')
    elif thing != '@everyone' and thing != '@here':
        await client.say(str(counterf) + " respects payed since bot start.")

@client.command(pass_context = True)
async def t(ctx, *args):
    global countert
    thing = ''
    author = ctx.message.author.mention
    for arg in args:
        thing = thing + arg + ' '
    thing = thing[:-1]
    if thing == '':
        await client.say(author + ' gave thanks.')
        countert += 1
    elif thing == '@everyone' or thing == '@here':
        await client.say('Really nibba')
    else:
        if thing == 'the bus driver':
            await client.say(author + ' has thanked ' + thing + ' on the way to victory!')
            countert += 1
        else:
            await client.say(author + ' has thanked ' + thing + ".")
            countert += 1
    if countert == 1 and thing != '@everyone' and thing != '@here':
        await client.say('Wow! You are the first to thank since bot has started.')
    elif thing != '@everyone' and thing != '@here':
        await client.say(str(countert) + " thanks given since bot start.")

@client.command(pass_context = True)
async def df(ctx, *args):
    global counterdf
    thing = ''
    author = ctx.message.author.mention
    for arg in args:
        thing = thing + arg + ' '
    thing = thing[:-1]
    if thing == '':
        await client.say(author + ' has disrespected.')
        counterdf += 1
    elif thing == '@everyone' or thing == '@here':
        await client.say('I disrespect you')
    else:
        await client.say(author + ' has disrespected ' + thing + ".")
        counterdf += 1
    if counterdf == 1 and thing != '@everyone' and thing != '@here':
        await client.say('Wow! You are the first to disrespect since bot has started.')
    elif thing != '@everyone' and thing != '@here':
        await client.say(str(counterdf) + " disrespects since bot start.")

@client.command()
async def count(*args):
    if len(args) == 0:
        await client.say(str(counterf) + " respects since bot start.")
        await client.say(str(countert) + " thanks since bot start.")
        await client.say(str(counterdf) + " disrespects since bot start.")
        await client.say(str(counterf + countert + counterdf) + " total actions since bot start")
    else:
        what = args[0]
        if what == 'f' or what == 'respect' or what == 'respects':
            await client.say(str(counterf) + " respects since bot start.")
        elif what == 't' or what == 'thank' or what == 'thanks':
            await client.say(str(countert) + " thanks since bot start.")
        elif what == 'df' or what == 'disrespect' or what == 'disrespects':
            await client.say(str(counterdf) + " disrespects since bot start.")
        elif what == 'total':
            await client.say(str(counterf + countert + counterdf) + " total actions since bot start")

@client.command()
async def invite():
    await client.say("Invite Respecc Bot to your server: https://discordapp.com/oauth2/authorize?client_id=496140572445245465&scope=bot&permissions=8")

@client.command()
async def commands():
    embed = discord.Embed(
        title = "Commands",
        description = "Respecc Bot Commands",
        colour = discord.Colour.blue()
    )

    embed.set_footer(text = "Bot made by .over#8908, add me as a friend for help or bug reporting.")

    embed.add_field(name = '!f', value = '!f <optional thing> | Respect something', inline = False)
    embed.add_field(name = '!t', value = '!t <optional thing> | Thank something', inline = False)
    embed.add_field(name = '!df', value = '!df <optional thing> | Disrespect something', inline = False)
    embed.add_field(name = '!count', value = '!count <f, t, df, total> | See the amount of actions done since last bot start.', inline = False)
    embed.add_field(name = '!invite', value = 'Invite the bot to your server!')

    await client.say(embed = embed)

client.run(TOKEN)