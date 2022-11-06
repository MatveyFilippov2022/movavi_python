import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
is_game = True
while is_game:
    computer = [random.choice(cards)]
    player = [random.choice(cards)]
    score = 0
    get_card = "у"
    while get_card == "у":
        player.append(random.choice(cards))
        if sum(player) > 21 and 11 in player:
            """Если туз в руке и сумма > 21"""
            for i in range (0, len(player)):
                if player[i] == 11:
                   player[i] = 1
                   break
    score = sum(player)
    print(f"Твоя рука: {player}, Очков:{score}")
    print(f"Первая компьютера:", computer[0])
    if score > 21:
        get_card = "n"
    else:
        get_card = input("y - Взять карту, n = оставить: ")
        computer.append(random.choice(cards))
        if sum (computer)[1] == 11:
            computer[1] = 1
            break
    score_computer = sum(computer)
    print("=" * 10)
    print(f" твоя итоговая рука:{player}.Очков:{score_computer}




