# from bset import settings
from dotenv import dotenv_values
config = dotenv_values(".env")
import discord
from blogic import *

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
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
        await message.channel.send("1) Recycle, Mendaur ulang plastik")
        await message.channel.send("2) Reduce, Mengurangi plastik")
        await message.channel.send("3) Reuse, menggunakan ulang plastik")
    elif message.content.startswith('$penjelasan 1'):
        await message.channel.send("Memanfaatkan kembali sampah setelah mengalami proses pengolahan.")
        await message.channel.send("Kamu bisa menggunakan botol plastik bekas untuk membuat patung, pot tanaman, tempat pensil, dan banyak hal lain!")
        await message.channel.send("Bisa juga dengan kertas bekas dijadikan karya lipat.")
    elif message.content.startswith('$penjelasan 2'):
        await message.channel.send("Penggunaan plastik selama beberapa dekade ini terus meningkat, dan aku yakin kamu pasti tidak mau menjadi salah satu penyumbang sampah plastik itu. Jadi ini lah beberapa cara yang bisa kamu lakukan agar dapat mengurangi penggunaan sampah plastik:")
        await message.channel.send("A) Menggunakan kantong belanja sendiri seperti shopper bag/degradeable plastic, Kantong plastik memang lebih praktis tapi hal ini lah yang membuat sampah plastik menjadi semakin menumpuk.")
        await message.channel.send("B) Membawa tumbler")
        await message.channel.send("C) Tidak menggunakan sedotan plastik")
        await message.channel.send("D) Hindari membeli makanan dan minuman menggunakan wada berbahan plastik")
    elif message.content.startswith('$penjelasan 3'):
        await message.channel.send("Penggunaan ulang plastik mengacu pada praktik memanfaatkan kembali produk-produk plastik yang sudah ada, seperti botol atau kantong, untuk tujuan lain setelah mereka diproses. Hal ini membantu mengurangi limbah plastik dan mengurangi tekanan terhadap lingkungan.")
        await message.channel.send("Beberapa contoh penggunaan ulang plastik:")
        await message.channel.send("A) Menggunakan kembali botol atau kantong plastik untuk menyimpan makanan atau barang-barang kecil di rumah.")
        #await message.channel.send("B) Melakukan refill atau isi ulang botol-botol plastik dengan air minum untuk mengurangi penggunaan botol plastik sekali pakai.")

client.run(config["TOKEN"])