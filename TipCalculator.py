# This is a tip calculator

print("Welcome to the tip calculator.\n")
bill = float(input("What was the total bill?\n $"))
tip = int(input("\nWhat percentage tip would you like to give? 10, 12, or 15?\n"))
people = int(input("\nHow many people to split the bill?\n"))

tip_costs = (bill / 100) * tip
final_bill = bill + tip_costs
costs_per_person = round(float(final_bill) / float(people), 2)
print(f"\nEach person should pay:\n${costs_per_person}")
