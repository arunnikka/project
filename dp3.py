# Contoh data
berat = [2, 3, 4, 5]
nilai = [3, 4, 5, 6]
kapasitas = 5

def knapsack_simple(berat, nilai, kapasitas):
    n = len(berat) 
    dp = [0] * (kapasitas + 1)
    pilihan = [[False] * (kapasitas + 1) for _ in range(n)]
    

    for i in range(n):
        for w in range(kapasitas, berat[i] - 1, -1): # dimulai dari index paling akhir dikurangyi dengan index paling kecil
            if dp[w - berat[i]] + nilai[i] > dp[w]:
                dp[w] = dp[w - berat[i]] + nilai[i]
                pilihan[i][w] = True
                
    # Melacak total berat barang yang dipilih
    w = kapasitas
    total_berat = 0
    for i in range(n - 1, -1, -1):
        if pilihan[i][w]:
            total_berat += berat[i]
            w -= berat[i]

    return dp[kapasitas], total_berat

# Eksekusi fungsi
nilai_maksimal, total_berat = knapsack_simple(berat, nilai, kapasitas)

# Output
print("Nilai maksimal:", nilai_maksimal)
print("Total berat barang yang dipilih:", total_berat)
