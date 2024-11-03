#import the random number generator module
import random

#generate a random number between 0 and 1, with 1 inclusive
toss = random.randint(0,1)

#conditional statement
if toss == 1:
  print("Heads")
if toss == 0:
  print("Tails")