## Inputs we need from the user
# Total rent
# Total food ordered for snacks
# Electricity units spend
# Charge per unit
# Persons living in the room/flat

## Output 
# Total amount you have to pay is

rent = int(input("Enter your room/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
elec_spend = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in the room/flat = "))

total_bill = elec_spend * charge_per_unit

output = (food + total_bill + rent) // persons

print("Each person will pay = ", output)