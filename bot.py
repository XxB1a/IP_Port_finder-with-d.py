from discord.ext import commands
from discord.ext.commands impport Bot
import time
import socket
import discord

token     = 'your_bots_token'
botdescr  = 'some_description'
prefix    = 'some_prefix_like_!'
bot       = commands.Bot(command_prefix=prefix, description=botdescr)

@bot.command()
async def findip(ctx, times : int = 1, port : int = 22):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if ctx.author.id == your_id:
        for i in range(int(times)):
            ip = f"{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"

            try:
                s.connect((ip, int(port)))
                s.settimeout(1)

                date = time.strftime("%I:%M:%S %p", time.localtime())
                print(f'Discovered {ip}:{port} at {date}')

                await ctx.send(f'Discovered {ip}:{port} at {date}')

            except:
                await asyncio.sleep(1)
                print(f'Oop! {ip}:{port} doesn\'t seem to be working!')

            finally:
                s.close()
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    else:
        await ctx.send('You cant do this silly')
        
@bot.event
async def on_ready():
    print(f'Logged in at {bot.user.name}! My ID is {bot.user.id}, i believe!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} servers!"))

bot.run(token)
