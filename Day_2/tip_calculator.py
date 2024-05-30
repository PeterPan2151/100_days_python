print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people are splitting the bill? "))

increment = (bill) * (tip / 100)
final_bill = bill + increment

print(f"Each perosn should pay: ${round(final_bill / people, 2)}")