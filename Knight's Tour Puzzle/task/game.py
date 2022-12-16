
def check_position():
    while True:
        try:
            x, y = input("Enter the knight's starting position: ").split()
            x, y = int(x), int(y)
            if 1 <= x <= 8 and 1 <= y <= 8:
                return x, y
            else:
                print("Invalid dimensions!")
        except ValueError:
            print("Invalid dimensions!")


x,y = check_position()


print("-" * 20)
for i in range(8, 0, -1):
    print(f"{i}|", end=" ")
    for j in range(8):
        if (j + 1) == x and i == y:
            print("X ", end="")
        else:
            print( "_ ", end="")
    print("|")
print("-" * 20)
print("   1 2 3 4 5 6 7 8")