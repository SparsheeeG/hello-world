import time
import sys

print("Welcome!")
time.sleep(1)
go = input("Enter Y to continue!\n")
if go.upper() == 'Y':
  pass
else:
  go = input("Enter Y to continue!\n")

name = input("First things first, what is your name?\n")
if name.title() != 'Audrey':
  print(f"Nice to meet you, {name}")
  time.sleep(1)
  relationship = None
  while relationship == None:
    relationship = input("Are you single or taken?\n")
    if relationship.title() == 'Taken':
      print("Congratulations! Wishing you and your partner the best <3!")    
    elif relationship.title() == 'Single':    
      looking = None
      while looking == None:
        looking = input("Are you currently looking for a relationship? Y/N\n")
        if looking.upper() == 'Y':
          print("You are eligible for the dating app! Contact Sparsh to register now!")
        elif looking.upper() == 'N':
          print("Sorry, you are not eligible for this dating app. Thanks for your participation!")
        else:
          looking = None
    else:
      relationship = None
elif name.title() == 'Audrey':
  print(f"Nice to meet you, {name}")
  time.sleep(1)
  relationship = None
  while relationship == None:
    relationship = input("Are you single or taken?\n")
    if relationship.title() == 'Taken':
      print("Congratulations! Wishing you and your partner the best <3!")    
    elif relationship.title() == 'Single':    
      looking = None
      while looking == None:
        looking = input("Are you currently looking for a relationship? Y/N\n")
        if looking.upper() == 'Y':
          prom = None
          while prom == None:
            prom = input("So prom's coming up soon... you want to go with me? Y/N\n")
            if prom.upper() == 'Y':
              print("Say yes on Discord!")
            elif prom.upper() == 'N':
              print("Was worth a try... Dauntless?")
            else:
              prom = None
        elif looking.upper() == 'N':
          prom = None
          while prom == None:
            prom = input("So prom's coming up soon... you want to go as friends? Y/N\n")
            if prom.upper() == 'Y':
              print("Say yes on Discord!")
            elif prom.upper() == 'N':
              print("Was worth a try... Dauntless?")
            else:
              prom = None
