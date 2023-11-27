import random

if __name__ == '__main__' :
    height = 5
    width = 5
else:
    height = 100
    width = 100

glider_pattern = [[0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0],
                  [0, 0, 0, 1, 0],
                  [0, 1, 1, 1, 0],
                  [0, 0, 0, 0, 0]]

glider_gun_pattern = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


life_model = [[0]*width for _ in [0]*height]
grid_model = life_model

for i in range(height):
    for j in range(width):
        life_model[i][j] = random.randint(0,1)

# life_model[1][2] = 1
# life_model[2][3] = 1
# life_model[3][1] = 1
# life_model[3][2] = 1
# life_model[3][3] = 1

def randomize():
    for i in range(height):
        for j in range(width):
            grid_model[i][j] = random.randint(0, 1)

def load_pattern(pattern, x_offset=0, y_offset=0):
    global  grid_model

    clear()

    j = y_offset

    for row in pattern:
        i = x_offset
        for value in row:
            grid_model[i][j] = value
            i += 1
        j += 1


def print_model(model):
    for i in model:
        print(i)

def gen_index(i, j, max_i, max_j):
    combo = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for n, m in combo:
        if (0 <= i + n  < max_i and
            0 <= j + m  < max_j):
            yield (n + i, m + j)


# print(new_model)

def next_gen():
    global grid_model, height, width

    updated_model = [[0]*width for _ in [0]*height]
    for i in range(height):
        for j in range(width):
            neighbor = 0
            for n, m in gen_index(i, j, height, width):
                neighbor += grid_model[n][m]
            if 1 < neighbor < 4:
                if neighbor == 3:
                    updated_model[i][j] = 1
                else :
                    updated_model[i][j] = grid_model[i][j]
            else:
                updated_model[i][j] = 0

    grid_model = updated_model

def clear():
    global grid_model, height, width


    grid_model = [[0 for j in range(width)] for i in range(height)]


if __name__ == '__main__' :
    print_model(life_model)
    print('-------------------')
    next_gen()
    print_model(grid_model)
    print('-------------------')
    next_gen()
    print_model(grid_model)
    print('-------------------')
    next_gen()
    print_model(grid_model)
    print('-------------------')
    clear()
    print_model(grid_model)
    print('-------------------')