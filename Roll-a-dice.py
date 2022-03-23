import random
from urllib import response

dice = input("roll a dice or not")
y = dice

def roll_the_dice(response):
    while response == "y":
        no = random.randint(1, 6)