prices = [7,6,4,3,1]
maxProfit = 0
for i in range(0, len(prices)-1):
    if(prices[i+1]>prices[i]):
        maxProfit = maxProfit + (prices[i+1]-prices[i])
print(maxProfit)
    