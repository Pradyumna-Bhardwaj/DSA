prices = [7,6,4,3,1]

const calcBestPrice = (prices) => {
    let low = prices[0]
    let max_profit = 0
    for (let i = 0; i < prices.length; i++){

        if(prices[i]-low>max_profit){
            max_profit = prices[i] - low
            console.log(max_profit, prices[i], low)
        }

        if(prices[i]<low){
            low = prices[i]
        }
        
    }
    return max_profit;
}


console.log(calcBestPrice(prices))