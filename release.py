import discord
from discord.ext import commands

TOKEN = 'reallylol'

counterf = 0

countert = 0

counterdf = 0

counterr = 0

version = 2.01

client = commands.Bot(command_prefix = '!')

client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name = '!commands', type=2))
    print ("Loaded up.")

"""Embed template
countert += 1
        embed = discord.Embed(
        description = author + ' gave thanks.',
        colour = discord.Colour.blue()
    )
        if counterf == 1:
            embed.set_footer(text = "Wow! You are the first to pay respects since bot start.")
        else:
            embed.set_footer(text = str(counterf) + " respects payed since bot start.")
        await client.say(embed = embed)
"""

@client.command(pass_context = True, aliases = ['respect'])
async def f(ctx, *args):
    global counterf
    thing = ''
    author = ctx.message.author.mention
    for arg in args:
        thing = thing + arg + ' '
    thing = thing[:-1]

    if thing == '':
        counterf += 1
        embed = discord.Embed(
        description = author + ' has paid their respects.',
        colour = discord.Colour.blue()
    )
        if counterf == 1:
            embed.set_footer(text = "Wow! You are the first to pay respects since bot start.")
        else:
            embed.set_footer(text = str(counterf) + " respects payed since bot start.")
        await client.say(embed = embed)
    
    elif thing == '@everyone' or thing == '@here':
        counterf += 1
        embed = discord.Embed(
        description = author + ' tells everyone to pay their respects.',
        colour = discord.Colour.blue()
    )
        if counterf == 1:
            embed.set_footer(text = "Wow! You are the first to pay respects since bot start.")
        else:
            embed.set_footer(text = str(counterf) + " respects payed since bot start.")
        await client.say(embed = embed)
    
    else:
        counterf += 1
        embed = discord.Embed(
        description = author + ' has paid their respects to ' + thing + ".",
        colour = discord.Colour.blue()
    )
        if counterf == 1:
            embed.set_footer(text = "Wow! You are the first to pay respects since bot start.")
        else:
            embed.set_footer(text = str(counterf) + " respects payed since bot start.")
        await client.say(embed = embed)

@client.command(pass_context = True, aliases = ['thank', 'thanks'])
async def t(ctx, *args):
    global countert
    thing = ''
    author = ctx.message.author.mention
    for arg in args:
        thing = thing + arg + ' '
    thing = thing[:-1]

    if thing == '':
        countert += 1
        embed = discord.Embed(
        description = author + ' gave thanks.',
        colour = discord.Colour.blue()
    )
        if countert == 1:
            embed.set_footer(text = "Wow! You are the first to thank since bot start.")
        else:
            embed.set_footer(text = str(countert) + " thanks given since bot start.")
        await client.say(embed = embed)
    
    elif thing == '@everyone' or thing == '@here':
        countert += 1
        embed = discord.Embed(
        description = author + ' tells everyone to give thanks.',
        colour = discord.Colour.blue()
    )
        if countert == 1:
            embed.set_footer(text = "Wow! You are the first to thank since bot start.")
        else:
            embed.set_footer(text = str(countert) + " thanks given since bot start.")
        await client.say(embed = embed)
    
    else:
        if thing == 'the bus driver':
            countert += 1
            embed = discord.Embed(
            description = author + ' thanked the bus driver on the way to victory!.',
            colour = discord.Colour.blue()
        )
            if countert == 1:
                embed.set_footer(text = "Wow! You are the first to thank since bot start.")
            else:
                embed.set_footer(text = str(countert) + " thanks given since bot start.")
            await client.say(embed = embed)
        else:
            countert += 1
            embed = discord.Embed(
            description = author + ' thanked ' + thing + '.',
            colour = discord.Colour.blue()
        )
            if countert == 1:
                embed.set_footer(text = "Wow! You are the first to thank since bot start.")
            else:
                embed.set_footer(text = str(countert) + " thanks given since bot start.")
            await client.say(embed = embed)

@client.command(pass_context = True, aliases = ['disrespect'])
async def df(ctx, *args):
    global counterdf
    thing = ''
    author = ctx.message.author.mention
    for arg in args:
        thing = thing + arg + ' '
    thing = thing[:-1]
    if thing == '':
        counterdf += 1
        embed = discord.Embed(
        description = author + ' disrespected.',
        colour = discord.Colour.blue()
    )
        if counterdf == 1:
            embed.set_footer(text = "Wow! You are the first to disrespect since bot start.")
        else:
            embed.set_footer(text = str(counterdf) + " disrespects since bot start.")
        await client.say(embed = embed)
    elif thing == '@everyone' or thing == '@here':
        counterdf += 1
        embed = discord.Embed(
        description = author + ' told everyone to disrespect',
        colour = discord.Colour.blue()
    )
        if counterdf == 1:
            embed.set_footer(text = "Wow! You are the first to disrespect since bot start.")
        else:
            embed.set_footer(text = str(counterdf) + " disrespects since bot start.")
        await client.say(embed = embed)
    else:
        counterdf += 1
        embed = discord.Embed(
        description = author + ' has disrespected ' + thing + ".",
        colour = discord.Colour.blue()
    )
        if counterdf == 1:
            embed.set_footer(text = "Wow! You are the first to disrespect since bot start.")
        else:
            embed.set_footer(text = str(counterdf) + " disrespects since bot start.")
        await client.say(embed = embed)

@client.command(pass_context = True, aliases = ['rip'])
async def r(ctx, *args):
    global counterr
    thing = ''
    author = ctx.message.author.mention
    for arg in args:
        thing = thing + arg + ' '
    thing = thing[:-1]

    if thing == '':
        counterr += 1
        embed = discord.Embed(
        description = author + ' says rip.',
        colour = discord.Colour.blue()
    )
        if counterr == 1:
            embed.set_footer(text = "Wow! You are the first to say rip since bot start.")
        else:
            embed.set_footer(text = str(counterr) + " rips since bot start.")
        await client.say(embed = embed)
    
    elif thing == '@everyone' or thing == '@here':
        counterr += 1
        embed = discord.Embed(
        description = author + ' tells everyone to put rips in the chat.',
        colour = discord.Colour.blue()
    )
        if counterr == 1:
            embed.set_footer(text = "Wow! You are the first to say rip since bot start.")
        else:
            embed.set_footer(text = str(counterr) + " rips since bot start.")
        await client.say(embed = embed)
    
    else:
        counterr += 1
        embed = discord.Embed(
        description = author + ' says rip ' + thing + ".",
        colour = discord.Colour.blue()
    )
        if counterr == 1:
            embed.set_footer(text = "Wow! You are the first to say rip since bot start.")
        else:
            embed.set_footer(text = str(counterr) + " rips since bot start.")
        await client.say(embed = embed)

@client.command(aliases = ['amount', 'actions'])
async def count(*args):
    if len(args) == 0:
        embed = discord.Embed(
        colour = discord.Colour.blue()
    )
        embed.add_field(name = 'Respects', value = counterf, inline = False)
        embed.add_field(name = 'Thanks', value = countert, inline = False)
        embed.add_field(name = 'Disrespects', value = counterdf, inline = False)
        embed.add_field(name = 'Rips', value = counterr, inline = False)
        embed.set_footer(text = str(counterf + countert + counterdf + counterr) + " total actions since bot start.")

        await client.say(embed = embed)
    else:
        what = args[0]
        if what == 'f' or what == 'respect' or what == 'respects':
            embed = discord.Embed(
            description = str(counterf) + " respects since bot start.",
            colour = discord.Colour.blue()
        )
            await client.say(embed = embed)
        elif what == 't' or what == 'thank' or what == 'thanks':
            embed = discord.Embed(
            description = str(countert) + " thanks since bot start.",
            colour = discord.Colour.blue()
        )
            await client.say(embed = embed)
        elif what == 'df' or what == 'disrespect' or what == 'disrespects':
            embed = discord.Embed(
            description = str(counterdf) + " disrespects since bot start.",
            colour = discord.Colour.blue()
        )
            await client.say(embed = embed)
        elif what == 'r' or what == 'rip' or what == 'rips':
            embed = discord.Embed(
            description = str(counterr) + " rips since bot start.",
            colour = discord.Colour.blue()
        )
            await client.say(embed = embed)
        elif what == 'total':
            embed = discord.Embed(
            description = str(counterf + countert + counterdf + counterr) + " total actions since bot start",
            colour = discord.Colour.blue()
        )
            await client.say(embed = embed)

@client.command()
async def invite():
    await client.say("Invite Respecc Bot to your server: https://discordapp.com/oauth2/authorize?client_id=496140572445245465&scope=bot&permissions=8")

@client.command(aliases = ['servercount'])
async def servers():
    serverCount = len(client.servers)
    await client.say("The bot is in " + str(serverCount) + " servers.")

@client.command()
async def help():
    await client.say("Add .over#8908 as a friend for help, or do !commands to see a list of commands.")

@client.command()
async def commands():
    embed = discord.Embed(
        title = "Commands",
        description = "Respecc Bot Commands",
        colour = discord.Colour.blue()
    )

    embed.set_footer(text = "Bot made by .over#8908, add me as a friend for help or bug reporting.")

    embed.add_field(name = '!f', value = '!f [optional thing] | Respect something', inline = False)
    embed.add_field(name = '!t', value = '!t [optional thing] | Thank something', inline = False)
    embed.add_field(name = '!df', value = '!df [optional thing] | Disrespect something', inline = False)
    embed.add_field(name = '!count', value = '!count [f, t, df, total] | See the amount of actions done since last bot start.', inline = False)
    embed.add_field(name = '!invite', value = 'Invite the bot to your server!')

    await client.say(embed = embed)

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name = 'Mcславяне')
    await client.add_roles(member, role)

client.run(TOKEN)
