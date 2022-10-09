# Линкор - 1 (4)
# Крейсер - 2 (3)
# Эсминец - 3 (2)

# структура списка:
# x, y, есть ли корабль, есть ли попадание

# field
field_size = 4

field1 = []
field2 = []
# field

# fleet
# fleet

def create_field(field_size):
    for i in range(0, field_size):
        for j in range(0, field_size):
            field1.append([i, j, False, False])
            field2.append([i, j, False, False])


def create_field_test():
    s = 4
    for i in range(0, s):
        for j in range(0, s):
            field1.append([i, j, False, False])
            field2.append([i, j, False, False])
    print(field1)
    print()
    print(field2)

def place_ships():
    pass

def place_ships_test():
    test_ships = [['рыбацкая лодка', 4, 1], ['плот', 2, 2]]
    for i in range(0, len(test_ships)):
        for j in range(0, test_ships[i][2]):
            print('Местоположение носа корабля', test_ships[i][0], '(длина', test_ships[i][1], '):', end=' ')
            while True:
                # проверка на читаемость
                try:
                    str = input()
                    coords = str.split()
                    coords = list(map(int, coords))
                    print(coords)
                except ValueError:
                    print('Координаты нечитаемые')
                    print('Введите координаты ещё раз:', end=' ')
                    continue
                # проверка на читаемость
                else:
                    # проверка на размещение носа
                    coord_list_number = -1
                    can_be_placed = False
                    for k in range(0, len(field1)):
                        if coords[0] == field1[k][0] and coords[1] == field1[k][1]:
                            if field1[k][2] == False:
                                coord_list_number = k
                                can_be_placed = True

                    if can_be_placed == False:
                        print('Корабль не может быть размещен')
                        print('Введите координаты ещё раз:', end=' ')
                        continue
                    # проверка на размещение носа

                    # проверка на размещение всего корабля
                    if test_ships[i][1] > 1:
                        while True:
                            print('Выберите направление носа:')
                            print('N - вверх')
                            print('S - вниз')
                            print('W - влево')
                            print('E - вправо')

                            str = input()
                            ship_coords = []
                            offset = 0
                            if str == 'N' or str == 'S' or str == 'W' or str == 'E':
                                if str == 'N':
                                    offset = -1
                                elif str == 'S':
                                    offset = 1
                                elif str == 'W':
                                    offset = -field_size
                                elif str == 'E':
                                    offset = field_size

                                ship_coords.append(coords)

                                # первое смещение
                                sequence_coord_list_number = coord_list_number + offset
                                new_coords = []
                                new_coords.append(field1[sequence_coord_list_number][0])
                                new_coords.append(field1[sequence_coord_list_number][1])
                                ship_coords.append(new_coords)
                                if abs(ship_coords[0][0] - ship_coords[1][0]) > 1 or abs(ship_coords[0][1] - ship_coords[1][1]) > 1:
                                    print('Корабль выходит за границы поля битвы')
                                    continue
                                if field1[sequence_coord_list_number][2] == True:
                                    print('Корабль врезается в другой корабль')
                                    continue
                                # первое смещение

                                # последующие смещения
                                mistake = False
                                for k in range(1, test_ships[i][1] - 1):
                                    sequence_coord_list_number += offset
                                    new_coords = []
                                    new_coords.append(field1[sequence_coord_list_number][0])
                                    new_coords.append(field1[sequence_coord_list_number][1])
                                    ship_coords.append(new_coords)
                                    if abs(ship_coords[k][0] - ship_coords[k + 1][0]) > 1 or abs(ship_coords[k][1] - ship_coords[k + 1][1]) > 1:
                                        print('Корабль выходит за границы поля битвы')
                                        mistake = True
                                        break
                                    if field1[sequence_coord_list_number][2] == True:
                                        print('Корабль врезается в другой корабль')
                                        mistake = True
                                        break
                                if mistake == True:
                                    continue
                                # последующие смещения

                                can_be_fully_placed = True

                                # размещение
                                if can_be_fully_placed == True:
                                    field1[coord_list_number][2] = True
                                    sequence_coord_list_number = coord_list_number + offset
                                    field1[sequence_coord_list_number][2] = True
                                    for k in range(1, test_ships[i][1] - 1):
                                        sequence_coord_list_number += offset
                                        field1[sequence_coord_list_number][2] = True
                                    print(field1)
                                    break
                                # размещение
                            else:
                                continue
                    # проверка на размещение всего корабля
                    break

create_field(field_size)
place_ships_test()