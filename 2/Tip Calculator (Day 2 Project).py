# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6

# Format the result to 2 decimal places = 33.60

# Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
amount_people = int(input("How many people to split the bill? "))

# total_bill = (estimated_bill / amount_people) * (tip/ 100)
# rounded_total_bill = round(total_bill, 2)

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / amount_people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)


print(f"Each person should pay: ${final_amount}")
