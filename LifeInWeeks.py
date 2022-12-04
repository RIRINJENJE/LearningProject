# This calculator shows you how many days,weeks, and months you have left in your life.
# (if you live till the age of 90)

age = input("What is your current age? ")

age_int = int(age)

years_left = 90 - age_int
days = years_left * 365
weeks = years_left * 52
months = years_left * 12

message = f"You have {days} days, {weeks} weeks, and {months} months left."
print(message)