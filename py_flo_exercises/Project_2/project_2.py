print("--------------------------------")
print("----- FINANCIAL VISUALIZER -----")
print("--------------------------------")
salary = input("Annual Salary:\n")
housing = input("Monthly Housing:\n")
bills = input("Monthly Bills:\n")
food = input("Weekly Food:\n")
travel = input("Annual Travel:\n")

def isvalid(check):
    for letter in check:
        if letter.isnumeric() == False and letter != '.':
            return True
    return False

if isvalid(salary) or isvalid(housing) or isvalid(bills) or isvalid(food) or isvalid(travel):
    print("Invalid input, please try again.")
else:
    print("All inputs confirmed valid.")

salary = float(salary)
housing = float(housing)
bills = float(bills)
food = float(food)
travel = float(travel)
tax = 0

if salary >= 0 and salary <= 10000:
    tax = round(salary * 0.05, 2)
elif salary >= 10001 and salary <= 40000:
    tax = round(salary * 0.1, 2)
elif salary >= 40001 and salary <= 80000:
    tax = round(salary * 0.15, 2)
else:
    tax = round(salary * 0.2, 2)

annual_housing = housing * 12
annual_bills = bills * 12
annual_food = food * 12
extra = salary - (housing + bills + food + travel + tax)

percentage_housing = (annual_housing / salary) * 100
percentage_bills = (annual_bills / salary) * 100
percentage_food = (annual_food / salary) * 100
percentage_travel = (travel / salary) * 100
percentage_tax = (tax / salary) * 100
percentage_extra = (extra / salary) * 100


print("-----------------------------------------------------------------------")
print(f"housing | $ {annual_housing:.2f} |  {percentage_housing:.1f} % | ")
print(f"bills   |  $ {annual_bills:.2f} |    {percentage_bills:.1f} % | ")
print(f"food    |  $ {annual_food:.2f} |    {percentage_bills:.1f} % | ")
print(f"travel  |  $ {travel:.2f} |   {percentage_travel:.1f} % | ")
print(f"tax     |  $ {tax:.2f} |      {percentage_tax:.1f} % | ")
print(f"extra   |  $ {extra:.2f} |     {percentage_extra:.1f} % | ")
# Tutaj pisz swój kod, młody padawanie ;-)
