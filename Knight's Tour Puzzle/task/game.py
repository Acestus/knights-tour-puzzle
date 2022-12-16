
def check_board_size():
    while True:
        try:
            column, row = input("Enter your board dimensions: ").split()
            column, row = int(column), int(row)
            if column > 0 and row > 0:
                return column, row
            else:
                print("Invalid dimensions!")
        except ValueError:
            print("Invalid dimensions!")
            continue
def check_position(column, row):
    while True:
        try:
            x, y = input("Enter the knight's starting position: ").split()
            x, y = int(x), int(y)
            if 1 <= x <= column and 1 <= y <= row:
                return x, y
            else:
                print("Invalid dimensions!")
        except ValueError:
            print("Invalid dimensions!")

def next_move(x, y, column, row):
    possible_moves = []
    if x - 2 > 0 and y - 1 > 0:
        possible_moves.append((x - 2, y - 1))
    if x - 2 > 0 and y + 1 <= row:
        possible_moves.append((x - 2, y + 1))
    if x - 1 > 0 and y - 2 > 0:
        possible_moves.append((x - 1, y - 2))
    if x - 1 > 0 and y + 2 <= row:
        possible_moves.append((x - 1, y + 2))
    if x + 1 <= column and y - 2 > 0:
        possible_moves.append((x + 1, y - 2))
    if x + 1 <= column and y + 2 <= row:
        possible_moves.append((x + 1, y + 2))
    if x + 2 <= column and y - 1 > 0:
        possible_moves.append((x + 2, y - 1))
    if x + 2 <= column and y + 1 <= row:
        possible_moves.append((x + 2, y + 1))
    return possible_moves

column, row = check_board_size()
x,y = check_position(column, row)
cell_size = len(str(column * row))
length = column * (cell_size + 1) + 3
print("Here are the possible moves:")
print("-" * length)
for i in range(row, 0, -1):
    print(f"{i}|", end=" ")
    for j in range(column):
        if (j + 1) == x and i == y:
            print(" " * (cell_size - 1) + "X", end=" ")
        elif (j + 1, i) in next_move(x, y, column, row):
            print(" " * (cell_size - 1) + "O", end=" ")
        else:
            print( "_" * cell_size, end=" ")
    print("|")
print("-" * length)
print("   ", end="")
for i in range(column):
    print(f" {i + 1} ", end="")