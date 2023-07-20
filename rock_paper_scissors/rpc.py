import random
choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
pc = random.randint(0,2)
print(pc)

if choose != 2 and choose < pc or choose == 2 and pc == 0:
    print("Sorry you lost...")
elif choose == pc:
    print("It's a draw.")
else:
    print("Congrats! You won.")
    