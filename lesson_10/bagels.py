import random

life = 10  # жизней
length = 3  # три символа

answer = random.randint(100, 999)  # ответ
answer = str(answer)  # перевели в тип данных строка

    while life: # пока жизни != 0
        is_guessed = False
        print("=" * 10)

        print("Жизней:", end="")
        for i in range(life):
            print("❤", end="")
            uess = input("Предположение:")
        if len(guess) != length or not guess.isdigit(): # если длина != 3 или не число
            print("Число от 100 до 999")
            continue # перезапускаем цикл

        if guess == answer:
            print("Пабеда 🏆")
            is_guessed = True
            break

        if not is_guessed: # если не отгадал
            # проверка на fermi
            for i in range(length): #от 0 до 2 включительно
                if guess[i]



