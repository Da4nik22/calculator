print("выберите действие:")
print("1. вычитание")
print("2. сложение") 
print("3. деление")
print("4. умножение")

action = int(input("выберите действие (1-4): "))
number1 = int(input("введите 1-е число: "))
number2 = int(input("введите 2-е число: "))

if action == 1:  
    result = number1 - number2
elif action == 2:  
    result = number1 + number2
elif action == 3:
    if number2 != 0:  
        result = number1 / number2
    else:
        result = "error"
elif action == 4:
    result = number1 * number2
else:
    result = "error"

print("Вычисление...")
print("Вычисление...")
print("Вычисление...")
print(f"итог: {result}")