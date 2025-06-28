func maxProfit(prices []int) int {
    minPrice := prices[0]
    profit := 0

    for _, val := range prices{
        if val < minPrice {
            minPrice = val
        }

        if val - minPrice > profit {
            profit = val - minPrice
        }
    }

    return profit
}