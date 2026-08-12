print("Это простой калькулятор. Доступные операции: +  -  *  /  >  <  ==")
a = float(input("Введите первое число: "))
operation = input("Введите операцию: ")
b = float(input("Введите второе число: "))

if operation == "+":
    result = a + b
    print("Результат:", result)
elif operation == "-":
    result = a - b
    print("Результат:", result)
elif operation == "*":
    result = a * b
    print("Результат:", result)
elif operation == "/":
    result = a / b
    print("Результат:", result)
elif operation == ">":
    if a > b:
        print(a, "больше", b)
    elif a < b:
        print(a, "меньше", b)
    else:
        print(a, "равно", b)
elif operation == "<":
    if a < b:
        print(a, "меньше", b)
    elif a > b:
        print(a, "больше", b)
    else:
        print(a, "равно", b)
elif operation == "==":
    if a == b:
        print(a, "равно", b)
    else:
        print(a, "не равно", b)
else:
    print("Неизвестная операция")