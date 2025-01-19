# Contoh penggunaan
weights = [2, 3, 4, 5]  # Berat item
values = [3, 4, 5, 6]   # Nilai item
capacity = 5            # Kapasitas maksimal
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

print("Nilai maksimum yang dapat dibawa:", knapsack(weights, values, capacity))