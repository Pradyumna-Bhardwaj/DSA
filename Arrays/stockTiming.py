prices = [7,1,5,3,6,4]

currProfit = 0
maxProfit = 0
minPrice = prices[0]
for i in range(len(prices)):
    minPrice = min(minPrice, prices[i])
    currProfit = prices[i] - minPrice
    maxProfit = max(currProfit, maxProfit, 0)
print(maxProfit)
