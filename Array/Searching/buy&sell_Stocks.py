# define a function
def findMaxProfit(price):
    minPrice = float('inf')
    print(minPrice)
    maxProfit = 0
    for i in range(len(price)):
        if price[i] < minPrice:
            minPrice = price[i]
        elif price[i]-minPrice > maxProfit:
            maxProfit = price[i]-minPrice
    return maxProfit


# driver code
price = [7, 1, 5, 3, 6, 20, 16]
result = findMaxProfit(price)
print(result)
