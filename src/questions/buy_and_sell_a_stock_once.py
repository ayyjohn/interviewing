def buy_and_sell_a_stock_once(prices: list[float]) -> float:
    if len(prices) == 0:
        return 0

    max_profit = float("-inf")
    min_price = prices[0]

    for price in prices:
        print(price, min_price, max_profit)
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit
