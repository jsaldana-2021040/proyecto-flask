coins = [1, 2, 5, 10, 20, 50]

resultado = [0, 0, 0, 0, 0, 0]

def getCoins(num):    
    while num > 0:
        maxCoin = max(coin for coin in coins if coin <= num)
        maxCoinIndex = coins.index(maxCoin)
        resultado[maxCoinIndex] += 1
        num -= maxCoin
    
    return resultado

print(getCoins(15))