import discord
from discord.ext import commands, tasks
import time
import asyncio
from webserver import keep_alive
from dotenv import load_dotenv
import os
import random
import traceback
version = 'v2.7.4'
load_dotenv()
keep_alive()

#Fill up these values to use the selfbot
self_bot_prefix="."                 #Change your prefix if you don't like it
token = os.getenv("TOKEN")          #Don't enter your token here, see README.md file to know how to enter token
channelid= 1071656675850854510      #Enter the channel id where you want the owo self bot to work
ownerid = 866186448309583903        #Enter the owner's id who will control this selfbot


bot = commands.Bot(command_prefix=self_bot_prefix)
owoid=408785106942164992
intervals = [2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6]
flip = [9.0,10.0,11.0,12.0,13.0,14.0]
owoh = [14.0,15.0,16.0,17.0,18.0,19.0,20.0]
channelid=int(channelid)
ownerid=int(ownerid)
@tasks.loop(seconds=random.choice(intervals))
async def spam():
    channel = bot.get_channel(int(channelid))
    await asyncio.sleep(random.choice(owoh))
    await channel.send('owoh')
    def check(message):
        return message.author.id==owoid and message.channel==channel
    try:
        reply=await bot.wait_for('message', check=check, timeout=30.0)
    except asyncio.TimeoutError:
        print("Owo didn't reply")
        user=bot.get_user(ownerid)
        await user.send(f"Owo bot didn't replied. Turning off myself. Use {self_bot_prefix}grind to wake me up")
        spam.cancel()
        return
    print(f"succefully owoh")
    await asyncio.sleep(random.choice(owoh))
    await channel.send('owo sell all')
    def check(message):
        return message.author.id==owoid and message.channel==channel
    try:
        reply=await bot.wait_for('message', check=check, timeout=30.0)
    except asyncio.TimeoutError:
        print("Owo didn't reply")
        user=bot.get_user(ownerid)
        await user.send(f"Owo bot didn't replied. Turning off myself. Use {self_bot_prefix}grind to wake me up")
        spam.cancel()
        return
    print(f"succefully sell")
    await channel.send('owo flip 500')
    def check(message):
        return message.author.id==owoid and message.channel==channel
    try:
        reply=await bot.wait_for('message', check=check, timeout=30.0)
    except asyncio.TimeoutError:
        print("Owo didn't reply")
        user=bot.get_user(ownerid)
        await user.send(f"Owo bot didn't replied. Turning off myself. Use {self_bot_prefix}grind to wake me up")
        spam.cancel()
        return
    print(f"succefully owo flip 500")
    await asyncio.sleep(random.choice(flip))
    await channel.send('owo cash')
    def check(message):
        return message.author.id==owoid and message.channel==channel
    try:
        reply=await bot.wait_for('message', check=check, timeout=30.0)
    except asyncio.TimeoutError:
        print("Owo didn't reply")
        user=bot.get_user(ownerid)
        await user.send(f"Owo bot didn't replied. Turning off myself. Use {self_bot_prefix}grind to wake me up")
        spam.cancel()
        return
    print(f"succefully cash")
    await asyncio.sleep(random.choice(flip))


@spam.before_loop
async def before_spam():
    await bot.wait_until_ready()

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online")
    bot.db = await aiosqlite.connect("owo.db")
    await bot.db.execute(
        "CREATE TABLE IF NOT EXISTS owos (command str)")
    print("owos table created!!")
    cur = await bot.db.execute("SELECT command from owos")
    res = await cur.fetchone()
    if res is None:
        await bot.db.execute("INSERT OR IGNORE INTO owos (command) VALUES (?)",("hold",))
    elif res[0]=="hold":
        spam.cancel()
    elif res[0]=="grind":
        spam.start()
    await bot.db.commit()
    
@bot.event
async def on_message(message):
    if message.guild:
        if message.channel.id== channelid:
            if message.author.id==owoid:
                if f"{bot.user.name}! Please complete your captcha" in message.content:
                    member = message.guild.get_member(bot.user.id)
                    if f"{member.display_name}! Please complete your captcha" in message.content:
                        spam.cancel()
                        cur = await bot.db.execute("SELECT command from owos")
                        res = await cur.fetchone()
                        if res is None:
                            await bot.db.execute("INSERT OR IGNORE INTO owos (command) VALUES (?)",("hold",))
                        else:
                            await bot.db.execute("UPDATE owos SET command = ?",("hold",))
                        await bot.db.commit()
            elif message.author.id==ownerid:
                if f"{self_bot_prefix}say" in message.content:
                    msg = message.content.split(" ",1)[1]
                    await message.channel.send(msg)
                elif f"{self_bot_prefix}grind" in message.content:
                    await message.delete()
                    await message.channel.send("Ok, let's go")
                    spam.start()
                    cur = await bot.db.execute("SELECT command from owos")
                    res = await cur.fetchone()
                    if res is None:
                        await bot.db.execute("INSERT OR IGNORE INTO owos (command) VALUES (?)",("grind",))
                    else:
                        await bot.db.execute("UPDATE owos SET command = ?",("grind",))
                    await bot.db.commit()
                elif f"{self_bot_prefix}hold" in message.content:
                    await message.delete()
                    await message.channel.send('Got it bro!')
                    spam.cancel()
                    cur = await bot.db.execute("SELECT command from owos")
                    res = await cur.fetchone()
                    if res is None:
                        await bot.db.execute("INSERT OR IGNORE INTO owos (command) VALUES (?)",("hold",))
                    else:
                        await bot.db.execute("UPDATE owos SET command = ?",("hold",))
                    await bot.db.commit()
        
    elif message.channel in bot.private_channels:
        if message.author.id==owoid:
            if "Are you a real human?" in message.content:
                spam.cancel()
                image = message.attachments[0]
                user=bot.get_user(ownerid)
                cur = await bot.db.execute("SELECT command from owos")
                res = await cur.fetchone()
                if res is None:
                    await bot.db.execute("INSERT OR IGNORE INTO owos (command) VALUES (?)",("hold",))
                else:
                    await bot.db.execute("UPDATE owos SET command = ?",("hold",))
                await bot.db.commit()
                await user.send(str(image))
            elif "I have verified that you are human! Thank you!" in message.content:
                msg = message.content
                user=bot.get_user(ownerid)
                await user.send(msg)
                cur = await bot.db.execute("SELECT command from owos")
                res = await cur.fetchone()
                if res is None:
                    await bot.db.execute("INSERT OR IGNORE INTO owos (command) VALUES (?)",("grind",))
                else:
                    await bot.db.execute("UPDATE owos SET command = ?",("grind",))
                await bot.db.commit()
                spam.start()
            elif f"{self_bot_prefix}grind" in message.content:
                spam.start()
                cur = await bot.db.execute("SELECT command from owos")
                res = await cur.fetchone()
                if res is None:
                    await bot.db.execute("INSERT OR IGNORE INTO owos (command) VALUES (?)",("grind",))
                else:
                    await bot.db.execute("UPDATE owos SET command = ?",("grind",))
                await bot.db.commit()
            elif f"{self_bot_prefix}hold" in message.content:
                spam.cancel()
                cur = await bot.db.execute("SELECT command from owos")
                res = await cur.fetchone()
                if res is None:
                    await bot.db.execute("INSERT OR IGNORE INTO owos (command) VALUES (?)",("hold",))
                else:
                    await bot.db.execute("UPDATE owos SET command = ?",("hold",))
                await bot.db.commit()
                
        elif message.author.id==ownerid:
            text = message.content.strip()
            if "captcha" in text.lower():
                captcha=text.split(" ",1)[1]
                await bot.user.send(captcha)
            

try:
    bot.run(f"{token}")
except discord.HTTPException:
    while True:
        time.sleep(10)
        os.system("kill 1")
except:
    traceback.print_exc()
