stocks = [7,1,5,3,6,4]

# O(N*2) solution - not optimised
def max_profit(stocks):
    max_profit = 0
    current_profit = 0
    for i in range(len(stocks)):
        for j in range(i+1, len(stocks)):
            if stocks[j] > stocks[i]:
                current_profit = stocks[j] - stocks[i]
                max_profit = max(max_profit, current_profit)
    return max_profit


print(max_profit(stocks))


# optimised version
def max_profit_optimised(stocks):
    min_price = stocks[0]
    max_profit = 0
    for i in range(1, len(stocks)):
        profit = stocks[i] - min_price
        max_profit = max(profit, max_profit)
        min_price = min(min_price, stocks[i])
    return max_profit

print(max_profit_optimised(stocks))