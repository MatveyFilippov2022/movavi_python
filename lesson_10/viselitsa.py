import random

vocabulary = ['Anton', 'Alex', 'Alexandr', 'Arsalan', 'Danil', 'Kirill', 'Sergey', 'Nikolay', 'Nasty', 'Natasha',
              'Ivan', 'Igor', 'Gosha', 'Galina', 'Olya', 'Oksana', 'Oleg', 'James', 'Bill']
word_answer = random.choice(vocabulary)

# создание отображаемого слова
word_display = []
for i in range(len(word_answer)):
    word_display.append("_")  # добавить _ в список

counter = 0  # счётчик проявленных букафф
life = 7
print(word_display)

while counter != len(word_answer) and life > 0:  # пока кол-во проявленных букв != кол-ву всех букв и есть жизни
    letter = input("Буква: ")
    letter_is_be = False
    for i in range(len(word_answer)):  # пробегаемся по слову
        if letter == word_answer[i]:  # если буква равна букве из слова
            if word_display[i] != "_":  # если буква отгадана
                letter_is_be = True  # буква уже была

            else:  # если буква не отгадана
                word_display[i] = letter  # проявляем букву
                counter += 1  # то же самое, что и counter = counter + 1
                letter_is_be = True  # буква есть в слове
    if not letter_is_be:  # если не угадал
        life = life - 1
    print(word_display)
if counter == len(word_answer):  # если отгадали все буквы
    print("Ты победил! 😎")
else:
    print("Проиграл, получается. 😟")