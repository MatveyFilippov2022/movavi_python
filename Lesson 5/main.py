#
# # # x = 7
# # # # if - если
# # # # elese - иначе
# # # if x <= 10 or x == : # икс меньше или равно десяти
# # #     print("Икс не больше 10 или равен 15")
# # # else:
# # #     print("Икс больше 10") input
# # # x = int(input("Введи число: "))
# # # if x < 0:
# # #     print("Отрицательное")
# # # elif x > 0: # elif - else if = иначе если
# # #     print ("Положительное")
# # # else:
# # #     print("Нолик")
# # #
# # # year =int(input(""))
/# print (отрицательный
# # number_1 = int(input("Ведиди первое число:")
# # operation = input("Введи операцию(+, -, *, /,):")
# # number_2 = int(input("Ведиди второе число:")
# #
# # lst = ["+", "-", "/", "*"] # список допустимых операций
# # if operation in lst: # если операция В списке опепраций
# #     if operation == "+": # операция сложение
# #         print(number_1 + number_2)
# number_1 = int(input("Ведиди первое число:")
# number_2 = int(input("Ведиди второе число:")
# number_3 = int(input("Ведиди третье число:")
#
# lst = [number_1, number_2, number_3]
# mini = min(lst) #поиск минимального
# maxi = max(lst) #поиск максимального
#
# print("Минимальное: ", mini)
# print("Минимальное: ", maxi)
ticket = input("Введи номер билета:")
if len(ticket) == 6:
    first_half = ticket[:3] # первые три числа
    second_half = ticet[-3:] # последние три числа

    first_sum = int(first_half[0]) +int(first_half[1]) +int(first_half[2])
    second_sum == int(second_half[0]) +int(second_half[1]) +int(second_half[2])

    if first_sum == second_sum:
        print("Твой билет счасливый!")
    else:
        print("Не повезло не фортануло(")
else:
    print("Не то ты ввёл!")

