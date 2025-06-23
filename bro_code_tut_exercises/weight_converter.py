weight = float(input("Enter your weight: "))
kg_lb = input("kg or lb?: ")

if kg_lb == 'kg':
    lb = weight * 2.20
    print(f"Your weight in lb is : {round(lb,2)}")
elif kg_lb == 'lb':
    kg = weight / 2.20
    print(f"Your weight in kg is : {round(kg,2)}")
else:
    print(f"{kg_lb} not valid")

