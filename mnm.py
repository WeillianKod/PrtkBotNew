import discord
import os
import random
from dotenv import dotenv_values
from blogic import *
from discord.ext import commands

config = dotenv_values(".env")
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Kita telah masuk sebagai {bot.user}')

item = os.listdir("__pycache__/images")

def images_acak():
    return random.choice(os.listdir("__pycache__/kreasi"))
def senyum_acak():
    return random.choice(os.listdir("__pycache__/sen"))

@bot.command()
async def contoh(ctx):
    with open(f"__pycache__/kreasi/{images_acak()}", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def halo(ctx):
    await ctx.send("Hi!")

@bot.command()
async def senyum(ctx):
    with open(f"__pycache__/sen/{senyum_acak()}", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def koin(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))


@bot.command()
async def ide(ctx):
    await ctx.send("Ya! Baiklah. Beberapa ide yang mungkin menarik:")
    await ctx.send("1) Recycle, mendaur ulang plastik")
    await ctx.send("2) Reduce, mengurangi plastik")
    await ctx.send("3) Reuse, menggunakan ulang plastik")
    with open(f"__pycache__/poster1.jpg", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def penjelasan1(ctx):
    await ctx.send("Memanfaatkan kembali sampah setelah mengalami proses pengolahan. Kamu bisa menggunakan botol plastik bekas untuk membuat patung, pot tanaman, tempat pensil, dan banyak hal lain! Bisa juga dengan kertas bekas dijadikan karya lipat.")

@bot.command()
async def penjelasan2(ctx):
    await ctx.send("Penggunaan plastik selama beberapa dekade ini terus meningkat, dan aku yakin kamu pasti tidak mau menjadi salah satu penyumbang sampah plastik itu. Jadi ini lah beberapa cara yang bisa kamu lakukan agar dapat mengurangi penggunaan sampah plastik.")
    await ctx.send("A) Menggunakan kantong belanja sendiri seperti shopper bag/degradeable plastic. Kantong plastik memang lebih praktis tapi hal ini lah yang membuat sampah plastik menjadi semakin menumpuk.")
    await ctx.send("B) Membawa tumbler saat berpergian, selain kamu bisa mengisi ulangnya dengan air, hal ini juga bisa menjadi salah satu kegiatan untuk mengurangi sampah plastik.")
    await ctx.send("C) Tidak menggunakan sedotan plastik, kamu dapat mengganti sedotan plastik dengan sedotan stainles steel, sedotan bambu, dan sedotan dari kertas untuk sedotan sekali pakai.")
    await ctx.send("D) Hindari membeli makanan dan minuman menggunakan wada berbahan plastik.")

@bot.command()
async def penjelasan3(ctx):
    await ctx.send("Penggunaan ulang plastik mengacu pada praktik memanfaatkan kembali produk-produk plastik yang sudah ada, seperti botol atau kantong, untuk tujuan lain setelah mereka diproses. Hal ini membantu mengurangi limbah plastik dan mengurangi tekanan terhadap lingkungan.")
    await ctx.send("Beberapa contoh penggunaan ulang plastik:")
    await ctx.send("A) Menggunakan kembali botol atau kantong plastik untuk menyimpan makanan atau barang-barang kecil di rumah.")
    await ctx.send("B) Melakukan refill atau isi ulang botol-botol bekas shampoo atau sabun dengan shampoo atau sabun untuk mengurangi sampah botol plastik.")

bot.run(config["TOKEN"])
