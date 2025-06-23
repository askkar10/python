num1 = float(input("Pierwsza liczba: "))
operator = input("Co chcesz zrobić? +,-,*,/: ")
num2 = float(input("Druga liczba: "))

if operator == '+':
    result = num1 + num2
    print(result)
elif operator == '-':
    result = num1 - num2
    print(result)
elif operator == '*':
    result = num1 * num2
    print(result)
elif operator == '/':
    result = num1 / num2
    print(result)
else:
    print(f"operator not valid")

