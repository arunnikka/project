berat = [2, 3, 4, 5]  
nilai = [3, 4, 5, 6]
kapasitas = 5          # Kapasitas knapsack
n = len(berat)         # Jumlah barang

def knapsack_bruteforce(berat, nilai, kapasitas, n):
    def knapsack_rekursif(i, kapasitas_sisa):
        if i == n or kapasitas_sisa == 0:
            return 0
        
        # Pilihan 1: tidak memilih barang ke-i
        tidak_ambil = knapsack_rekursif(i + 1, kapasitas_sisa)
        
        # Pilihan 2: memilih barang ke-i jika kapasitas memungkinkan
        ambil = 0
        if berat[i] <= kapasitas_sisa:
            ambil = nilai[i] + knapsack_rekursif(i + 1, kapasitas_sisa - berat[i])
        
        # Mengembalikan nilai maksimum antara memilih atau tidak memilih barang ke-i
        return max(tidak_ambil, ambil)

    return knapsack_rekursif(0, kapasitas)

hasil = knapsack_bruteforce(berat, nilai, kapasitas, n)
print("Nilai maksimal yang bisa diperoleh:", hasil)