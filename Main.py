# Import statement
import math


# ORGANIZE CODE BEFORE PROCEEDING FURTHER









      # implement images in text
      # print if a monster attacks
def printMonsterImage():
  print("███████████████████████████")
  print("███████▀▀▀░░░░░░░▀▀▀███████")
  print("████▀░░░░░░░░░░░░░░░░░▀████")
  print("███│░░░░░░░░░░░░░░░░░░░│███")
  print("██▌│░░░░░░░░░░░░░░░░░░░│▐██")
  print("██░└┐░░░░░░░░░░░░░░░░░┌┘░██")
  print("██░░└┐░░░░░░░░░░░░░░░┌┘░░██")
  print("██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██")
  print("██▌░│██████▌░░░▐██████│░▐██")
  print("███░│▐███▀▀░░▄░░▀▀███▌│░███")
  print("██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██")
  print("██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██")
  print("████▄─┘██▌░░░░░░░▐██└─▄████")
  print("█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████")
  print("████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████")
  print("█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████")
  print("███████▄░░░░░░░░░░░▄███████")
  print("██████████▄▄▄▄▄▄▄██████████")
  print("███████████████████████████")

  
def printFaceImage():
  print("---")
  print("\  \ ")
  print(" \  \ ")
  print("  \  \ ")
  print("   \  \ ")
  print("    \  \ ")
  print("     \  \ ")
  print("       [] ") 

# Telling user how to play
def showInstructions():
  # Print out an intro and main menu
  print("Welcome to : ")
  print("========")
  print("Commands: ")
  print("go '[direction]' to chose a path")
  print("get '[item]' to pick up an item")
  print("attack '[enemy]' with '[item]' to attack an enemy")
  
  # Player health.  Maybe change to "Healthy", "Near death", etc...
playerHealth = 50
print("-----------------------")
print("Please enter your name")
playerName = input()
print("-----------------------")

# Player's current status
def showStatus(playerHealth):
  print("-----------------------")
  print(playerHealth)
  print("You are in the " + rooms[currentRoom]["name"])
  if "item" in rooms[currentRoom]:
    print("You see " + str(rooms[currentRoom]["item"]))
    
  # Print current inventory
  # str is toString
  print("Inventory: " + str(inventory))
    
  # If an enemy is in the room...  
  if "enemy" in rooms[currentRoom]:
    
    print("You are confronted by a " + rooms[currentRoom]["enemy"] + "!")
    
  print("What will you do?")
  print("-----------------------")
  printMonsterImage()
  return playerHealth

# An initially empty inventory array
inventory = ["rocks"]

# Currently equiped
currentEquip = []

# Using dictionaries to make a room
room = { "name" : "Hall" }

# Getting the name of the room
roomName = room["name"]

# Mapping rooms to a room number
rooms = { 1 : { "name" : "Hall" } , 2 : { "name" : "Bedroom" }}

print(roomName)

# Adding doors/More rooms/Linking together rooms
# Add additional items to a room by adding to its dictionary
rooms = {
            1  : { 
                   "name"  : "Hall", # Being mapped to Hall
                   "east"  :  2 ,    # East being mapped to 2
                  "south"  :  3 ,
                  # Does not currently support two word items
                  "item"   : ["axe" , "bat" , "apple" , "family portrait" ] ,
                  "enemy"  : "Skeleton"
                 } ,
                
                
            2  : { 
                   "name"  : "Bedroom" ,
                   "west"  : 1 ,
                   "south" : 4 ,
                   "item"  : ["dressing table" , "bed" , "mirror"]
                 } ,
            
            
            
            3  : {  
                   "name"  : "Kitchen" ,
                   "north" : 1 ,
                   "item"  : "butcher knife",
                   "enemy" : "Skeleton" 
                 } ,
            
            
            
            4  : {  
                    "name" : "Bathroom" ,
                   "north" : 2 ,
                   "item"  : "mirror", 
                   "enemy" : "Skeleton"
                 }
        }
        
# Where the player statrs starts 
currentRoom = 1
        
showInstructions()

# An infitnite loop

while True:
  # Use error handling
  showStatus(playerHealth)
  try:
    action = input().lower().split()
  
  # Movement
    if action[0] == "go":
      if action[1] in rooms[currentRoom]:
        currentRoom = rooms[currentRoom][action[1]]
      else:
        print("You cannot go that way.")
        showStatus()
      
  # Other player actions    
    if action[0] == "get":
      print("ok")
      # If item is in the room and if the item is what the player enters
    if "item" in rooms[currentRoom] and action[1] in rooms[currentRoom]["item"]:
      print("ok 2")
      #if action[1] in rooms[currentRoom]:
      print("ok 3")
      inventory += [action[1]]
      # Deleting entire key, not allowing user to get other items...a problem
      # if action[1] in rooms[currentRoom]["item"]: del rooms[currentRoom]["item"]
      # Need to remove value from key after user takes it
      
  # Block to use item
    if action[0] == "use":
      if action[1] in inventory:
       print(playerName + " used " + str(action[1]))
      
  # Block to equip item
    if action[0] == "equip":
      if action[1] in inventory:
        print(playerName + " equiped " + str(action[1]))
      
  # Block to handle combat
    if action[0] == "attack":
      if action[1] in rooms[currentRoom]["enemy"]:
        print("")
      
      # If incorrect input, print error message to console
    break
  except TypeError:
    print("I cannot do that...")