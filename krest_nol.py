horizontal = [" ", "A", "B", "C"]     # выбор место положения x или 0  напоминает координаты,
# дабы игрок не путался взял на себя смелость переименовать 0 1 2 на A B C
first = ["0", "-", "-", "-"]
second = ["1", "-", "-", "-"]
third = ["2", "-", "-", "-"]
win_options = [     # список возможных побед
                        {"A0": "-", "A1": "-", "A2": "-"}, {"B0": "-", "B1": "-", "B2": "-"},
                        {"C0": "-", "C1": "-", "C2": "-"}, {"A0": "-", "B0": "-", "C0": "-"},
                        {"A1": "-", "B1": "-", "C1": "-"}, {"A2": "-", "B2": "-", "C2": "-"},
                        {"A0": "-", "B1": "-", "C2": "-"}, {"A2": "-", "B1": "-", "C0": "-"}]
br = 0      # флаг прекращения программы в случае победы


def pole():     # вывод поля на экран
    print(f'''{horizontal[0]:4} {horizontal[1]:7} {horizontal[2]:6} {horizontal[3]:7}''')
    print(f'''{first[0]:4} {first[1]:7} {first[2]:7} {first[3]:7}''')
    print(f'''{second[0]:4} {second[1]:7} {second[2]:7} {second[3]:7}''')
    print(f'''{third[0]:4} {third[1]:7} {third[2]:7} {third[3]:7}''')


def position(li, simvol):
    # определение позиции в списке(по горизонтали)
    if li[0] == "A":
        numinlist = 1
    elif li[0] == "B":
        numinlist = 2
    elif li[0] == "C":
        numinlist = 3
    else:
        perehod0 = input(f"Введено неверное значение {li} \n Ходит игрок № {igrok}. \nВыберите поле для {x_0}: ")
        position(perehod0.upper(), x_0)
        return False
    # определение списка(по вертикали)
    try:
        if li[1] == "0":
            sel_list = first
        elif li[1] == "1":
            sel_list = second
        elif li[1] == "2":
            sel_list = third
        else:
            perehod1 = input(f"Введено неверное значение {li} \n Ходит игрок № {igrok}. \nВыберите поле для {x_0}: ")
            position(perehod1.upper(), x_0)
            return False
    except IndexError:
        perehod1 = input(f"Введено неверное значение {li} \n Ходит игрок № {igrok}. \nВыберите поле для {x_0}: ")
        position(perehod1.upper(), x_0)
        return False
    if sel_list[numinlist] != '-':      # игрок ввел уже занятое поле
        perehod = input(f"Такой ход уже был \n Ходит игрок № {igrok}. \nВыберите поле для {x_0}: ")
        position(perehod.upper(), x_0)
    else:
        sel_list[numinlist] = simvol
        for i in range(len(win_options)):
            if li in win_options[i]:
                win_options[i][li] = simvol


pole()
for n in range(9):
    if n % 2 == 0:
        igrok = 1
        x_0 = "x"
    else:
        igrok = 2
        x_0 = "0"
    hod = input(f"Ходит игрок № {igrok}. \nВыберите поле для {x_0}: ")
    position(hod.upper(), x_0)
    pole()
    if n > 3:    # проверка начинается после 4го хода.
        win_del = []
        for j in range(len(win_options)):
            if "x" in win_options[j].values() and "0" not in win_options[j].values()\
                    and "-" not in win_options[j].values():
                print("Победил 1й игрок(x)")
                br = 1
                break
            elif "0" in win_options[j].values() and "x" not in win_options[j].values()\
                    and "-" not in win_options[j].values():
                print("Победил 2й игрок(0)")
                br = 1
                break
            if "x" in win_options[j].values() and "0" in win_options[j].values():
                win_del.append(j)
        win_del.reverse()
        for k in win_del:
            win_options.pop(k)
    if br == 1:
        break
    if n == 8:
        print("Ничья!")
