# Линкор - 1 (4)
# Крейсер - 2 (3)
# Эсминец - 3 (2)

# структура списка:
# x, y, есть ли корабль, есть ли попадание

# field
field_size = 8

field1 = []
field2 = []
# field

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