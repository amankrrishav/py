# Common Built-in Modules in Python Standard Library
# Python comes with "batteries included" — no pip install needed for these!

# 1. math module: Mathematical functions
import math

print("--- 1. math module ---")
print("math.sqrt(64) :", math.sqrt(64))    # 8.0
print("math.pow(2, 5) :", math.pow(2, 5))    # 32.0
print("math.ceil(4.2) :", math.ceil(4.2))    # 5 (round up)
print("math.floor(4.9):", math.floor(4.9))   # 4 (round down)
print("math.pi        :", round(math.pi, 4)) # 3.1416
print("math.factorial(5):", math.factorial(5)) # 120

# 2. random module: Pseudo-random number generators
import random

print("\n--- 2. random module ---")
print("random() [0.0 to 1.0)      :", round(random.random(), 3))
print("randint(1, 10) [inclusive] :", random.randint(1, 10))
print("choice from list           :", random.choice(["apple", "banana", "cherry"]))

cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print("shuffled list              :", cards)

# 3. datetime module: Date and time handling
from datetime import datetime, date

print("\n--- 3. datetime module ---")
now = datetime.now()
print("Current date & time:", now.strftime("%Y-%m-%d %H:%M:%S"))
print("Today's date       :", date.today())

# 4. os & sys modules: Operating system & Python runtime
import os
import sys

print("\n--- 4. os & sys modules ---")
print("Current Working Directory:", os.getcwd())
print("Python Version           :", sys.version.split()[0])
print("Platform                 :", sys.platform)
