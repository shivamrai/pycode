"""Best Time to Buy Sell Stock - Maximum profit from stocks."""


def max_profit(prices):
    """max_profit function."""
    if not prices or prices[-1] == min(prices[:-1]):
        return 0
    return prices[-1] - min(prices[:-1])


if __name__ == "__main__":
    a = [7, 1, 5, 3, 6, 4]
    print(min(a))
    print(a[-1])
