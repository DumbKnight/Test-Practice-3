# структура списка:
# x, y, есть ли корабль, есть ли попадание

# обозначения:
# # - неизвестное поле
# * - попадание по кораблю
# ~ - попадание в воду
# = - корабль
# % - уничтоженный корабль

# field
field_size = 0

field1 = []
field2 = []
# field

# ships
test_ships = [['рыбацкая лодка', 4, 1], ['плот', 2, 2]]
ships1 = [['Крейсер', 3, 1], ['Эсминец', 2, 2]]
ships2 = [['Линкор', 4, 1], ['Крейсер', 3, 2], ['Эсминец', 2, 3]]

ships = []
# ships

# fleet
fleet1 = []
fleet2 = []
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


def place_ships(field, ships):
    # флот
    if field == field1:
        fleet = fleet1
    else:
        fleet = fleet2

    fleet_size = 0
    for i in range(0, len(ships)):
        for j in range(0, ships[i][2]):
            fleet_size += 1

    for i in range(0, fleet_size):
        fleet.append([])

    fleet_size = 0
    sequence_coordinates_list = []
    # флот
    for i in range(0, len(ships)):
        for j in range(0, ships[i][2]):
            print('Местоположение носа корабля', ships[i][0], '(длина', ships[i][1], '):', end=' ')
            while True:
                # проверка на читаемость
                try:
                    string = input()
                    coordinates = string.split()
                    coordinates = list(map(int, coordinates))
                except ValueError:
                    print('Координаты нечитаемые')
                    print('Введите координаты ещё раз:', end=' ')
                    continue
                # проверка на читаемость
                else:
                    # проверка на размещение носа
                    coordinates_list_number = -1
                    can_be_placed = False
                    for k in range(0, len(field)):
                        if coordinates[0] == field[k][0] and coordinates[1] == field[k][1]:
                            if field[k][2] == False:
                                coordinates_list_number = k
                                can_be_placed = True

                    if can_be_placed == False:
                        print('Корабль не может быть размещен')
                        print('Введите координаты ещё раз:', end=' ')
                        continue
                    # проверка на размещение носа

                    # проверка на размещение всего корабля
                    if ships[i][1] > 1:
                        while True:
                            print('Выберите направление носа:')
                            print('N - вверх')
                            print('S - вниз')
                            print('W - влево')
                            print('E - вправо')

                            string = input()
                            ship_coordinates = []
                            offset = 0
                            if string == 'N' or string == 'S' or string == 'W' or string == 'E':
                                if string == 'N':
                                    offset = -1
                                elif string == 'S':
                                    offset = 1
                                elif string == 'W':
                                    offset = -field_size
                                elif string == 'E':
                                    offset = field_size

                                ship_coordinates.append(coordinates)

                                # первое смещение
                                sequence_coordinates_list_number = coordinates_list_number + offset
                                new_coordinates = []
                                new_coordinates.append(field[sequence_coordinates_list_number][0])
                                new_coordinates.append(field[sequence_coordinates_list_number][1])
                                ship_coordinates.append(new_coordinates)
                                if abs(ship_coordinates[0][0] - ship_coordinates[1][0]) > 1 or abs(
                                        ship_coordinates[0][1] - ship_coordinates[1][1]) > 1:
                                    print('Корабль выходит за границы поля битвы')
                                    continue
                                if field[sequence_coordinates_list_number][2] == True:
                                    print('Корабль врезается в другой корабль')
                                    continue
                                # первое смещение

                                # последующие смещения
                                mistake = False
                                for k in range(1, ships[i][1] - 1):
                                    sequence_coordinates_list_number += offset
                                    new_coordinates = []
                                    new_coordinates.append(field[sequence_coordinates_list_number][0])
                                    new_coordinates.append(field[sequence_coordinates_list_number][1])
                                    ship_coordinates.append(new_coordinates)
                                    if abs(ship_coordinates[k][0] - ship_coordinates[k + 1][0]) > 1 or abs(
                                            ship_coordinates[k][1] - ship_coordinates[k + 1][1]) > 1:
                                        print('Корабль выходит за границы поля битвы')
                                        mistake = True
                                        break
                                    if field[sequence_coordinates_list_number][2] == True:
                                        print('Корабль врезается в другой корабль')
                                        mistake = True
                                        break
                                if mistake == True:
                                    continue
                                # последующие смещения

                                can_be_fully_placed = True

                                # размещение
                                if can_be_fully_placed == True:
                                    sequence_coordinates_list = []
                                    fleet[fleet_size].append(ships[i][0])

                                    field[coordinates_list_number][2] = True
                                    sequence_coordinates_list_number = coordinates_list_number + offset
                                    field[sequence_coordinates_list_number][2] = True

                                    sequence_coordinates_list.append(coordinates_list_number)
                                    sequence_coordinates_list.append(sequence_coordinates_list_number)
                                    for k in range(1, ships[i][1] - 1):
                                        sequence_coordinates_list_number += offset
                                        field[sequence_coordinates_list_number][2] = True

                                        sequence_coordinates_list.append(sequence_coordinates_list_number)

                                    fleet[fleet_size].append(sequence_coordinates_list)
                                    hull_list =[]
                                    for k in range(0, len(sequence_coordinates_list)):
                                        hull_list.append(sequence_coordinates_list[k])
                                    fleet1[fleet_size].append(hull_list)
                                    fleet_size += 1
                                    break
                                # размещение
                            else:
                                continue
                    # проверка на размещение всего корабля
                    break


def place_ships_test():
    # флот
    ships_count = 0
    for i in range(0, len(test_ships)):
        for j in range(0, test_ships[i][2]):
            ships_count += 1
    print(ships_count)
    for i in range(0, ships_count):
        fleet1.append([])
    print(fleet1)
    ships_count = 0
    sequence_coordinates_list = []
    # флот
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
                                    sequence_coordinates_list = []
                                    fleet1[ships_count].append(test_ships[i][0])

                                    field1[coord_list_number][2] = True
                                    sequence_coord_list_number = coord_list_number + offset
                                    field1[sequence_coord_list_number][2] = True

                                    sequence_coordinates_list.append(coord_list_number)
                                    sequence_coordinates_list.append(sequence_coord_list_number)
                                    for k in range(1, test_ships[i][1] - 1):
                                        sequence_coord_list_number += offset
                                        field1[sequence_coord_list_number][2] = True

                                        sequence_coordinates_list.append(sequence_coord_list_number)

                                    fleet1[ships_count].append(sequence_coordinates_list)
                                    new_list = []
                                    for k in range(0, len(sequence_coordinates_list)):
                                        new_list.append(sequence_coordinates_list[k])
                                    fleet1[ships_count].append(new_list)
                                    print(field1)
                                    print(fleet1)
                                    ships_count += 1
                                    break
                                # размещение
                            else:
                                continue
                    # проверка на размещение всего корабля
                    break

def fire(field):
    if field == field1:
        fleet = fleet1
    else:
        fleet = fleet2

    while True:
        print('Координаты обстрела:', end=' ')

        # проверка на читаемость
        try:
            string = input()
            coordinates = string.split()
            coordinates = list(map(int, coordinates))
        except ValueError:
            print('Координаты нечитаемые')
            print('Введите координаты ещё раз:', end=' ')
            continue
        # проверка на читаемость
        else:
            # проверка возможности попадания
            coordinates_list_number = -1
            can_be_hitted = False
            for i in range(0, len(field)):
                if coordinates[0] == field[i][0] and coordinates[1] == field[i][1]:
                    if field[i][3] == False:
                        coordinates_list_number = i
                        can_be_hitted = True

            if can_be_hitted == False:
                print('Координаты не могут быть обстреляны')
                print('Введите координаты ещё раз:', end=' ')
                continue
            # проверка возможности попадания

            # регистрация попадания
            if field[coordinates_list_number][2] == False:
                print('Промах')
                field[coordinates_list_number][3] = True
                break
            else:
                print('Попадание')
                field[coordinates_list_number][3] = True

                # уничтожение корабля
                ship_number = -1
                is_found = False
                for i in range(0, len(fleet)):
                    for j in range(0, len(fleet[i][1])):
                        if fleet[i][1][j] == coordinates_list_number:
                            ship_number = i
                            is_found = True
                            fleet[i][1].remove(coordinates_list_number)
                            break
                    if is_found == True:
                        break

                if len(fleet[ship_number][1]) == 0:
                    print('Корабль', ships[ship_number][0], '(длина', ships[ship_number][1], ') был уничтожен')
                # уничтожение корабля
                continue
            # регистрация попадания

def fire_test():
    field = field1

    while True:
        print('Координаты обстрела:', end=' ')

        # проверка на читаемость
        try:
            string = input()
            #string = '0 0'
            coordinates = string.split()
            coordinates = list(map(int, coordinates))
        except ValueError:
            print('Координаты нечитаемые')
            print('Введите координаты ещё раз:', end=' ')
            continue
        # проверка на читаемость
        else:
            # проверка возможность попадания
            coordinates_list_number = -1
            can_be_hitted = False
            for i in range(0, len(field)):
                if coordinates[0] == field[i][0] and coordinates[1] == field[i][1]:
                    if field[i][3] == False:
                        coordinates_list_number = i
                        can_be_hitted = True

            if can_be_hitted == False:
                print('Координаты не могут быть обстреляны')
                print('Введите координаты ещё раз:', end=' ')
                continue
            # проверка возможность попадания

            # регистрация попадания
            if field[coordinates_list_number][2] == False:
                print('Промах')
                field[coordinates_list_number][3] = True
                break
            else:
                print('Попадание')
                field[coordinates_list_number][3] = True

                # уничтожение корабля
                ship_number = -1
                is_found = False
                for i in range(0, len(fleet1)):
                    for j in range(0, len(fleet1[i][1])):
                        print(fleet1[i][1])
                        if fleet1[i][1][j] == coordinates_list_number:
                            ship_number = i
                            is_found = True
                            print(fleet1)
                            fleet1[i][1].remove(coordinates_list_number)
                            print(fleet1)
                            break
                    if is_found == True:
                        break

                if len(fleet1[ship_number][1]) == 0:
                    for i in range(0, len(test_ships)):
                        if test_ships[i][2] > 1:
                            ship_number = ship_number - test_ships[i][2] + 1
                    print('Корабль', test_ships[ship_number][0], '(длина', test_ships[ship_number][1], ') был уничтожен')
                # уничтожение корабля
                continue
            # регистрация попадания


def print_field(field, is_placement, is_end):
    print_number = 0

    if field == field1:
        fleet = fleet1
    else:
        fleet = fleet2

    if is_placement == True:
        for i in range(0, int(len(field) / field_size)):
            for j in range(0, int(len(field) / field_size)):
                if field[j * field_size + i][2] == True:
                    print('=', end=' ')
                else:
                    print('~', end=' ')
            print()
    else:

        if is_end == False:
            for i in range(0, int(len(field) / field_size)):
                for j in range(0, int(len(field) / field_size)):
                    if field[j * field_size + i][3] == True:
                        if field[j * field_size + i][2] == True:
                            # в какой корабль попадание
                            for k in range(0, len(fleet)):
                                for l in range(0, len(fleet[k][2])):
                                    if fleet[k][2][l] == print_number:
                                        # уничтоженный корабль
                                        if len(fleet[k][1]) > 0:
                                            print('*', end=' ')
                                        else:
                                            print('%', end=' ')
                                        # уничтоженный корабль
                            # в какой корабль попадание
                        else:
                            print('~', end=' ')  # V
                    else:
                        print('#', end=' ')  # V
                    print_number += field_size
                print_number = print_number - pow(field_size, 2) + 1
                print()
        else:
            for i in range(0, int(len(field) / field_size)):
                for j in range(0, int(len(field) / field_size)):
                    if field[j * field_size + i][3] == True:
                        if field[j * field_size + i][2] == True:
                            # в какой корабль попадание
                            for k in range(0, len(fleet)):
                                for l in range(0, len(fleet[k][2])):
                                    if fleet[k][2][l] == print_number:
                                        # уничтоженный корабль
                                        if len(fleet[k][1]) > 0:
                                            print('*', end=' ')
                                        else:
                                            print('%', end=' ')
                                        # уничтоженный корабль
                            # в какой корабль попадание
                        else:
                            print('~', end=' ')
                    else:
                        if field[j * field_size + i][2] == True:
                            print('=', end=' ')
                        else:
                            print('~', end=' ')
                    print_number += field_size
                print_number = print_number - pow(field_size, 2) + 1
                print()


def print_field_test():
    number = 0
    field = field1
    is_placement = int(input())
    is_end = True
    if is_placement == 1:
        placement_bool = True
    else:
        placement_bool = False
    if placement_bool == True:
        for i in range(0, int(len(field) / field_size)):
            for j in range(0, int(len(field) / field_size)):
                if field[j * field_size + i][2] == True:
                    print('=', end=' ')
                else:
                    print('~', end=' ')
            print()
    else:
        if is_end == False:
            print(fleet1)
            print(number)
            for i in range(0, int(len(field) / field_size)):
                for j in range(0, int(len(field) / field_size)):
                    if field[j * field_size + i][3] == True:
                        if field[j * field_size + i][2] == True:
                            # в какой корабль попадание
                            for k in range(0, len(fleet1)):
                                for l in range(0, len(fleet1[k][2])):
                                    if fleet1[k][2][l] == number:
                                        # уничтоженный корабль
                                        if len(fleet1[k][1]) > 0:
                                            print('*', end=' ')
                                        else:
                                            print('%', end=' ')
                                        # уничтоженный корабль
                            # в какой корабль попадание
                        else:
                            print('~', end=' ')  # V
                    else:
                        print('#', end=' ')  # V
                    number += field_size
                number = number - pow(field_size, 2) + 1
                print()
        else:
            for i in range(0, int(len(field) / field_size)):
                for j in range(0, int(len(field) / field_size)):
                    if field[j * field_size + i][3] == True:
                        if field[j * field_size + i][2] == True:
                            # в какой корабль попадание
                            for k in range(0, len(fleet1)):
                                for l in range(0, len(fleet1[k][2])):
                                    if fleet1[k][2][l] == number:
                                        # уничтоженный корабль
                                        if len(fleet1[k][1]) > 0:
                                            print('*', end=' ')
                                        else:
                                            print('%', end=' ')
                                        # уничтоженный корабль
                            # в какой корабль попадание
                        else:
                            print('~', end=' ')
                    else:
                        if field[j * field_size + i][2] == True:
                            print('=', end=' ')
                        else:
                            print('~', end=' ')
                    number += field_size
                number = number - pow(field_size, 2) + 1
                print()
    print(field1)
