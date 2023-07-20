print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
number_of_people = int(input("How many people to split the bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

amount_to_pay = "{:.2f}".format(total/number_of_people + tip_percentage/100 * (total/number_of_people))

print(f"Each person should pay: ${amount_to_pay}")