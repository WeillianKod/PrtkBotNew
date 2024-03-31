import random

pchar = "#?300@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""

jumlah = int(input("Berapa kata passwormu:"))


for _ in range(jumlah):
    passa = random.choice(pchar)
    password = password + passa
    
print("Password rahasia anda:", password)