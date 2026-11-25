
nama_produk = ["Mouse A", "Keyboard B", "Mouse C", "Monitor D", "Mouse E"]

kategori = ["Mouse", "Keyboard", "Mouse", "Monitor", "Mouse"]

harga = [50000, 150000, 35000, 1500000, 45000]

cari_kategori = "Mouse"

harga_termurah = None
index_termurah = -1

for i in range(len(nama_produk)):
    if kategori[i] == cari_kategori:
        if harga_termurah is None or harga[i] < harga_termurah:
            harga_termurah = harga[i]
            index_termurah = i

if index_termurah != -1:
    print("Nama produk:", nama_produk[index_termurah])
    print("Harga:", harga_termurah)
else:
    print("Produk tidak ditemukan")
