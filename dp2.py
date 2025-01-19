berat= [2, 3, 4, 5]
nilai = [3, 4, 5, 6]
kapasitas = 5

def knapsack(barang, bobot, kapasitas):
    dp = [0] * (kapasitas + 1)  # Hanya gunakan satu array untuk menyimpan nilai maksimum
    for i in range(len(berat)):
        for w in range(kapasitas, berat[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - berat[i]] + bobot[i])
    return dp[kapasitas]
print("Nilai maksimum:", knapsack(berat, nilai, kapasitas))