import sys

def init(size):
    grid = []
    elem = size**2 - 1
    for i in range(size):
        grid.append([])
        for j in range(size):
            grid[i].append(elem)
            elem -= 1

    if size % 2 == 0:
        grid[-1][-2], grid[-1][-3] = grid[-1][-3], grid[-1][-2]

    grid[-1][-1] = size**2

    return grid

def show(grid):
    for line in grid:
        for elem in line:
            if elem == len(grid) ** 2:
                print("__ ", end="")
            else:
                print("{:0=2d} ".format(elem), end="")
        print()

def move(grid, tile):
    size = len(grid)
    for i in range(size):
        for j in range(size):
            if grid[i][j] == size**2:
                emptyX = i
                emptyY = j
            if grid[i][j] == tile:
                tileX = i
                tileY = j

    if abs(emptyX - tileX) + abs(emptyY - tileY) == 1:
        grid[emptyX][emptyY], grid[tileX][tileY] = grid[tileX][tileY], grid[emptyX][emptyY]

def won(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] - count != 1:
                return False
            count += 1
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2 or int(sys.argv[1]) < 0 or int(sys.argv[1]) > 9:
        print("usage: python fifteen.py size")
        exit(1)

    print("WELCOME TO THE GAME OF FIFTEEN")

    size = int(sys.argv[1])
    grid = init(size)

    while not won(grid):
        show(grid)
        tile = int(input("Enter a tile to move: "))
        if tile < 0:
            break
        move(grid, tile)

    show(grid)
    if won(grid):
        print("You have won!")
