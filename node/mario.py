def get_int():
    while True:
        print("height: ", end = "")
        n = int(input())
        if n >= 0 and n < 24:
            break
    return n

def main():
    hoogte = get_int()

    j = hoogte - 1

    for i in range(hoogte):
        print(" " * j, end = "")
        print("#" * (i + 2), end = "")
        print("")
        j = j - 1

if __name__ == "__main__":
    main()
