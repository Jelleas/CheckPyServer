if __name__ == "__main__":
    change = -1
    while change < 0:
        change = float(input("How much change is owed? "))
        change = int(round(change * 100))

    coins = [25, 10, 5, 1]
    nCoins = 0
    for coin in coins:
        nCoins += change // coin
        change %= coin

    print("{} coin(s) needed".format(nCoins))
