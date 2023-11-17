from random import randint




def menu():
    game_score = ["последняя игра ", "предыдущая игра", "прошлая игра"]
    score = {"player": 0,
             "computer": 0}
    if int(input("1 - начать игру\n2 - посмотреть игровой счет\n:")) == 1:
        start_game(score)
    else:
        sqr

    input()
    game_score.insert(0, score)
    game_score.pop()
    print()




menu()


def start_game(score):
    game = 0
    while game < 3:
        print(game)
        print()
        print("Счет:")
        for i,j in score.items():
            print(f"Игрок: {i}, Очков: {j}")

        print()
        player = int(input("Укажите орудие: 1 - ножницы, 2 - бумага , 3 - камень"))
        comp = randint(1,3)
        weapon = ["scissors","paper","rock"]
        print(weapon[comp - 1])

        if player == comp:
            print("ничья")
            score["player"] +=1
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
                score["player"] += 1
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
                score["player"] += 1
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
                score["player"] += 1
                game += 1
                continue

def sqr(game_score):



