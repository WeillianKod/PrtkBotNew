import random


def gen_pass(pass_length):
    elements = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ#@?"
    passe = ""

    for i in range(pass_length):
        passe += random.choice(elements)

    return passe

def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)

def flip_coin():
    flip = random.randint(0,2)
    if flip == 0:
        return "HEADS"
    else:
        return "TAILS"