import discord
from discord.ext import commands
import requests
import os
import random
from blogic import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def meme(ctx):
    List_file = os.listdir('__pycache__/images')
    rand_meme = random.choice(List_file)
    with open(f'__pycache__/images/{rand_meme}', 'rb') as f:
    # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def on_message(message):
    if message.content.startswith('$halo'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$senyum'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$koin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$ide'):
        await message.channel.send("Ya! Baiklah. Beberapa ide yang mungkin menarik:")
        await message.channel.send("1) Mendaur ulang plastik")
        await message.channel.send("2) Mengurangi plastik")
        await message.channel.send("3) Menggantikan plastik")

bot.run("MTIxNDE5MDUxNDg5MTUyNjE0NA.GeIDpF.MDZpgFBiUP-9iHbCQ6lEGsaBd-anKa08mYLx0I")