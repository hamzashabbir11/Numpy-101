Q NO 1

from karel.stanfordkarel import *

# File: warmup.py
# -----------------------------
# The warmup program defines a "main"
# function which currently just has one
# Command. Add two more commands to make karel: move(),
# pick_beeper(), move()
def main():
   move()
   # add your code here
   pick_beeper()
   move()

Q NO 2 

from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.
def main():
   move()
   turn_left()
   turn_left()
   turn_left()
   move()
   turn_left()
   move()
   move()
   pick_beeper()
   turn_left()
   turn_left()
   move()
   move()
   move()
   turn_left()
   turn_left()
   turn_left()
   move()
   

Q NO 3 

from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.
def main():
   move()
   picker()
   moverobo()
   picker()
   moverobo()
   picker()
   move()
   
      
   
def picker():
   for i in range(10):
      pick_beeper()
      
def moverobo():
   move()
   move()
      
 
  
