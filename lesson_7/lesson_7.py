# Виды ошибок

# ZeroDivisionErorr: divison by zero
# x = 15/0

# TypeError
# x = 15 + "a"

# indexError: list index out of range
# lst = [ 10, 5, 3]
# print(lst[3])

#SyntaxError
# if 5 > 0

# assert
# def summa(number: list[int]):
#     return sum(number)
#
# assert summa()
#
#
#
# try:
#     x = 5/0
# except ZeroDivisionError:
#     print("НА ноль делить низя")

# try - попытатся
# except - ожидать ошибки

# try:
#     x = 5/0 # первая ошибка. будет обработана
#     int("x") # вторая ошибка. не дойдём до неё (
#  except ZeroDivisionError:
#     print("ДЕление на ноль")
#
# except Exception: # обработается любая ошибка
#     print("Я обработаю всё.")
#
# try:  # попытатся
#     x = int(input("введи число:"))
# except ValueError:  # обработать ошибку
#     print("Э, уважаемый, хочу цифры!")
# else:     # мы не наткнулись на ошибку
#     print("Ура, победа. Ты не глуп.")
# finally:   # саботает всегда.
#     print("Кто я?")
#
# name = input("Введи имя:")
# if name == "Антон"
#     raise Exception("Антона нельзя") # вызвать союственную ошибку
# except Exception:
#     print("Одна ошибка и ты ошибся 🐺")
#     print("Ошибка-это фатальная:", error_message)

try:
    x = 5/0
except ZeroDivisionError:
    pass # пустышка-затычка


if 5 > 3: # если придумали условие
    pass # но не придумали что делать

temperatura = 50 # typo
print() # weak warning, пожелание