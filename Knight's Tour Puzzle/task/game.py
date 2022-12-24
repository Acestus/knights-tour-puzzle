def get_dimensions():
    while True:
        try:
            _columns, _rows = [int(num) for num in input('Enter your board dimensions:').split()]
            assert _columns > 0 and _rows > 0
        except (TypeError, ValueError, AssertionError):
            print("Invalid dimensions!")
        else:
            return _columns, _rows


def get_position():
    while True:
        try:
            _x, _y = [int(num) for num in input("Enter the knight's starting position:").split()]
            assert 1 <= _x <= columns and 1 <= _y <= rows
        except (TypeError, ValueError, AssertionError):
            print("Invalid position!")
        else:
            return _x, _y


def get_cell_size():
    if columns == 1:
        return 1
    elif columns < 9:
        return 2
    else:
        return 3


def get_possible_moves(start_x, start_y):
    steps = [[2, 1], [2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2], [-2, -1], [-2, 1]]
    moves = []
    for i in range(8):
        _x = start_x + steps[i][0]
        _y = start_y + steps[i][1]
        if _x in range(1, columns + 1) and _y in range(1, rows + 1):
            moves.append([_x, _y])
    return moves


def draw_possible_moves(_knight_moves, _visited_moves):
    for [_x, _y] in _knight_moves:
        num_moves = len(get_possible_moves(_x, _y)) - 1
        matrix[rows - _y][_x - 1] = ' ' * (cell_size - 1) + str(num_moves)
    for [_x, _y] in _visited_moves:
        matrix[rows - _y][_x - 1] = ' ' * (cell_size - 1) + '*'

def get_possible_moves_warnsdorff(start_x, start_y):
    steps = [[2, 1], [2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2], [-2, -1], [-2, 1]]
    moves = []
    for i in range(8):
        _x = start_x + steps[i][0]
        _y = start_y + steps[i][1]
        if _x in range(1, columns + 1) and _y in range(1, rows + 1):
            moves.append([_x, _y])
    return moves

def print_matrix(_matrix):
    sep_line = '-' * (columns * 3 + 3)  # '---------------' length depends on number_of_columns
    print(f' {sep_line}')
    for i in range(rows):
        print(rows - i, end='')
        print('|', *_matrix[i], '|')
    print(f' {sep_line}')
    bottom_line = [i for i in range(1, columns + 1)]  # '   1 2 3 ...... number_of_columns'
    print('  ', *bottom_line, sep=' ' * cell_size)
def print_matrix_warnsdorff(_matrix):
    #print("Matrix:", _matrix)
    sep_line = '-' * (columns * 3 + 3)  # '---------------' length depends on number_of_columns
    print(f' {sep_line}')
    for i in range(rows):
        print(rows - i, end='')
        print('|', *_matrix[i], '|')
    print(f' {sep_line}')
    bottom_line = [i for i in range(1, columns + 1)]  # '   1 2 3 ...... number_of_columns'
    print('  ', *bottom_line, sep=' ' * cell_size)
def get_next_move(visted):
    while True:
        try:
            _x, _y = [int(num) for num in input("Enter your next move").split()]
            assert 1 <= _x <= columns and 1 <= _y <= rows
            assert [_x, _y] not in visited_moves
        except (TypeError, ValueError, AssertionError):
            print("Invalid move!")
        if [_x, _y] not in get_possible_moves(x, y):
            print("Invalid move!", end=" ")
            continue
        else:
            return _x, _y

def give_me_an_answer():
    while True:
        try:
            _answer = input("Do you want to try the puzzle? (y/n): ")
            assert _answer in ['y', 'n']
        except AssertionError:
            print("Invalid answer!")
            continue
        if _answer == 'y':
            return True
        else:
            return False

def is_solution_possible(_columns, _rows):
    if _columns == 1 or _rows == 1:
        return True
    elif _columns == 2 and _rows == 2:
        return False
    elif _columns == 3 and _rows == 3:
        return False
    else:
        return True

def warnsdorff_rule(_x, _y, _visited_moves):
    possible_moves = get_possible_moves_warnsdorff(_x, _y)
    #print ("x:", _x, "y:", _y)
    possible_moves = [move for move in possible_moves if move not in _visited_moves]
    if possible_moves:
        possible_moves.sort(key=lambda move: len(get_possible_moves_warnsdorff(move[0], move[1])))
        #print ("Possible moves:", possible_moves)
        return possible_moves[0]
    else:
        return None



columns, rows = get_dimensions()
x, y = get_position()
answer = give_me_an_answer()
solution_exists = is_solution_possible(columns, rows)
cell_size = get_cell_size()

default_cell = '_' * cell_size  # depend on columns number default cell = '_' or '__' or '___'
matrix = [[default_cell] * columns for _ in range(rows)]  # create empty matrix(board)
matrix[rows - y][x - 1] = ' ' * (cell_size - 1) + 'X'  # draw start position on the board



print("User's tries:", answer)
print("The solution exists: ", solution_exists)
print("x = ", x, "y = ", y)
if answer is False:
    if solution_exists:
        print("\nHere's the solution!")
        # Use recursion to find the solution
        label = 1
        visited_moves = [[x, y]]
        while True:
            if label > 9:
                matrix[rows - y][x - 1] = '' * (cell_size - 1) + str(label)
            else:
                matrix[rows - y][x - 1] = ' ' * (cell_size - 1) + str(label)
            knight_moves = warnsdorff_rule(x, y, visited_moves)
            #print("Label:", label)

            if knight_moves is None:
                break
            else:
                x, y = knight_moves
                visited_moves.append([x, y])
                label += 1
            if len(visited_moves) == columns * rows:
                break
        if label > 9:
            matrix[rows - y][x - 1] = '' * (cell_size - 1) + str(label)
        else:
            matrix[rows - y][x - 1] = ' ' * (cell_size - 1) + str(label)
        print_matrix_warnsdorff(matrix)
    else:
        print("\nNo solution exists!")
else:
    if solution_exists:
        print("\nHere are the possible moves:")
        knight_moves = get_possible_moves(x, y)
        visited_moves = [[x, y]]
        draw_possible_moves(knight_moves, visited_moves)
        matrix[rows - y][x - 1] = ' ' * (cell_size - 1) + 'X'
        print_matrix(matrix)
        while True:
            visited_moves.append([x, y])
            matrix = [[default_cell] * columns for _ in range(rows)]  # create empty matrix(board)
            x, y = get_next_move(visited_moves)
            knight_moves = get_possible_moves(x, y)

            matrix[rows - y][x - 1] = ' ' * (cell_size - 1) + 'X'

            draw_possible_moves(knight_moves, visited_moves)
            print_matrix(matrix)
            print(f'Visited moves: {visited_moves}')
            print(f'Possible moves: {knight_moves}')
            if len(visited_moves) == columns * rows:
                print("What a great tour! Congratulations!")
                break
            for move in knight_moves:
                if move not in visited_moves:
                   break
            else:
                print("No more possible moves!")
                print(f"Your knight visited {len(visited_moves)} squares!")
                break
    else:
        print("\nNo solution exists!")
