print("Welcome to Treasure Island. \nYour mission is to find the treasure.")

start = input("You're at a cross road. Where do you wan to go? Type LEFT or RIGHT\n").upper()

if start == "LEFT":
    b = input("You come to a lake. There is an island in the middle of the lake. Type WAIT to wait for a boat. Type SWIM to swim across.\n").upper()
    if b == "WAIT":
        c = input("You arrive at the island unharmed. There is a house with 3 doors. One RED, one YELLOW and one BLUE. Which color do you choose?\n").upper()
        if c == "RED":
            print("It's a room full of fire. Game Over.")
        elif c == "BLUE":
            print("It's a room full of water. Game Over.")
        else: 
            print("You found the treasure!. Well done!")
    else:
        print("You enter a great storm. Game Over.")
else:
    print("Wrong way mate. Game Over")
