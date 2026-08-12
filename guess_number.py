import random
print("Игра «Угадай число»")
print("Компьютер загадал число от 1 до 20. Попробуй его угадать!")

secret_number = random.randint(1, 20)
attempts = 0  # счётчик попыток

while True:
    guess = input("Введи число от 1 до 20: ")
    guess = int(guess)
    attempts += 1
    if guess < secret_number:
        print("Загаданное число больше.")
    elif guess > secret_number:
        print("Загаданное число меньше.")
    else:
        print("Ты угадала!")
        print("Количество попыток:", attempts)
        break