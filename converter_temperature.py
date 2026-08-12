print("Это конвертер температуры: Цельсий - Фаренгейт")
print("Выберите вариант: 1 — Цельсий в Фаренгейт или 2 — Фаренгейт в Цельсий")

choice = input("Введите 1 или 2: ")
if choice == "1":
    celsius = float(input("Введите температуру в Цельсиях: "))
    fahrenheit = celsius * 9 / 5 + 32
    print("Температура в Фаренгейтах:", fahrenheit)
elif choice == "2":
    fahrenheit = float(input("Введите температуру в Фаренгейтах: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print("Температура в Цельсиях:", celsius)
else:
    print("Неверный выбор. Введите 1 или 2.")