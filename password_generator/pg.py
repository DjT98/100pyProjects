import random
import string

print("Welcome to Password Generator!")

num_of_letters = int(input("How many letters would you like in your password?\n"))
num_of_symbols = int(input("How many symbols would you like\n"))
num_of_numbers = int(input("How many numbers would you likeq\n"))

pw_gen = []

for char in range(1, num_of_letters + 1):
    pw_gen.append(random.choice(string.ascii_letters))

for char in range(1, num_of_symbols + 1):
    pw_gen += random.choice(string.punctuation)

for char in range(1, num_of_numbers + 1):
    pw_gen += random.choice(string.digits)

print(pw_gen)

random.shuffle(pw_gen)

print(pw_gen)

password = ""
for char in pw_gen:
    password += char

print(f"Your password is: {password}")

