
nama_produk = ["Mouse A", "Keyboard B", "Mouse C", "Monitor D", "Mouse E"]

kategori = ["Mouse", "Keyboard", "Mouse", "Monitor", "Mouse"]

harga = []

# Input harga setiap produk
for i in range(len(nama_produk)):
    print("Produk:", nama_produk[i])
    nilai = int(input("Masukkan harga: "))
    harga.append(nilai)

cari_kategori = "Mouse"

harga_termurah = None
index_termurah = -1

# Mencari produk termurah berdasarkan kategori
for i in range(len(nama_produk)):
    if kategori[i] == cari_kategori:
        if harga_termurah is None or harga[i] < harga_termurah:
            harga_termurah = harga[i]
            index_termurah = i

# Menampilkan hasil
if index_termurah != -1:
    print("Nama produk:", nama_produk[index_termurah])
    print("Harga:", harga_termurah)
else:
    print("Produk tidak ditemukan")
