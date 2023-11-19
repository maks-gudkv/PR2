from random import randint
import time


def sqr(game_score):
    while True:
        ch = int(input("укажите какую посмотреть игру 1 - последняя, 2 - предыдущая , 3 - прошлая\nЕсли хотете выйти - любое другое число :"))
        if ch != 1 and ch != 2 and ch != 3:
            return
        print()
        print(game_score[ch - 1])
        input("нажмите 'enter'")
        print()


def start_game(score):
    print()
    name = input("укажите имя: ")
    score[name] = score.pop("player")
    print()
    gm = int(input("укажите кол - во раундов:"))
    game = 0
    while game < gm:
        input("продолжить - 'enter'")
        print("______________________________________________")
        print("раунд:", game + 1)
        print()
        print("Счет:")
        for i,j in score.items():
            print(f"Игрок: {i}, Очков: {j}")

        print()
        player = int(input("Укажите орудие: 1 - ножницы, 2 - бумага , 3 - камень"))
        print()
        print("1")
        time.sleep(0.5)
        print("2")
        time.sleep(0.5)
        print("3")
        comp = randint(1,3)
        weapon = ("Ножницы","Бумага","Камень")
        print("орудие противника - ",weapon[comp - 1])
        print()

        if player == comp:
            print("ничья")
            score[name] +=1
            score["computer"] += 1
            game +=1
            continue

        if player == 1:
            if comp == 3:
                print("пройгрыш")
                score["computer"] += 1
                game += 1
                continue

            else:
                print("победа")
                score[name] += 1
                game += 1
                continue

        if player == 2:
            if comp == 1:
                print("пройгрыш")
                score["computer"] += 1
                game += 1
                continue
            else:
                print("победа")
                score[name] += 1
                game += 1
                continue

        if player == 3:
            if comp == 2:
                print("пройгрыш")
                score["computer"] += 1
                game += 1
                continue
            else:
                print("победа")
                score[name] += 1
                game += 1
                continue

    print("______________________________________________")
    print("игра закончена")
    print()
    if score[name] > score["computer"]:
        print("вы победили")
    elif score[name] < score["computer"]:
        print("вы проиграли")
    else:
        print("Ничья")

    print()
    print("Счет:")
    for i, j in score.items():
        print(f"Игрок: {i}, Очков: {j}")
    input("нажмите enter что бы продолжить")

    return score

def menu():
    game_score = ["последняя игра ---- ", "предыдущая игра ----", "прошлая игра---"]
    while True:
        score = {"player": 0,
                 "computer": 0}

        choce = int(input("1 - начать игру\n2 - посмотреть игровой счет\n:"))
        if choce == 1:
            start_game(score)
            game_score.insert(0, score)
            game_score.pop()
        elif choce == 2:
            sqr(game_score)




menu()

