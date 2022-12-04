# This is a tip calculator

print("Welcome to the tip calculator.\n")
bill = input("What was the total bill? $")
percentage = input("\nWhat percentage tip would you like to give? 10, 12, or 15?\n")
splitting = input("\nHow many people to split the bill?\n")

bill_as_float = float(bill)
percentage_as_int = int(percentage)
splitting_as_int = int(splitting)

tip_costs = (bill_as_float / 100) * percentage_as_int
final_bill = bill_as_float + tip_costs
costs_per_person = round(float(final_bill) / float(splitting), 2)
print(f"\nEach person should pay: ${costs_per_person}")
