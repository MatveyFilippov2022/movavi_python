alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_end = False
while not should_end: # пока should_end != True
    text = input("Введи свое сообщение: ").lower()
    text = list(text)  # преобразовать в список
    shift = int(input("Введи сдвиг:"))

    if shift = shift % len(alphabet) # сдвиг длины алфавита