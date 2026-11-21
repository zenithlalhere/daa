def knapsack(weights, values, W):
    """0-1 knapsack. Returns (best_value, chosen_item_indices)."""
    n = len(weights)
    # dp[i][w] = best value using first i items with capacity w
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        wt, val = weights[i - 1], values[i - 1]
        for w in range(W + 1):
            dp[i][w] = dp[i - 1][w]                     # skip item i
            if wt <= w:                                  # take item i if it fits
                dp[i][w] = max(dp[i][w], dp[i - 1][w - wt] + val)

    # backtrack to find which items were taken
    chosen, w = [], W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:                     # item i was taken
            chosen.append(i - 1)
            w -= weights[i - 1]
    chosen.reverse()
    return dp[n][W], chosen


if __name__ == "__main__":
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    W = 7
    best, items = knapsack(weights, values, W)
    print("Best value :", best)
    print("Items (0-indexed):", items)
