
# DATA MAHASISWA
mahasiswa = [
    ["1", "A", 85, 80, 90],
    ["2", "B", 90, 85, 80],
    ["3", "C", 75, 80, 85],
    ["4", "D", 80, 90, 95],
    ["5", "E", 95, 85, 90]
]

# INPUT NIM YANG DICARI
cari = input("Masukkan NIM yang ingin dicari: ")

# PROSES PENCARIAN
i = 0
ketemu = False

while i < len(mahasiswa):
    if mahasiswa[i][0] == cari:
        ketemu = True

        nim = mahasiswa[i][0]
        nama = mahasiswa[i][1]
        tugas = mahasiswa[i][2]
        uts = mahasiswa[i][3]
        uas = mahasiswa[i][4]

        # Menghitung nilai akhir
        akhir = (tugas + uts + uas) / 3

        # Menampilkan hasil
        print("\n===== DATA MAHASISWA =====")
        print("NIM         :", nim)
        print("Nama        :", nama)
        print("Nilai Tugas :", tugas)
        print("Nilai UTS   :", uts)
        print("Nilai UAS   :", uas)
        print("Nilai Akhir :", round(akhir, 2))

        break

    i += 1

# Jika NIM tidak ditemukan
if ketemu == False:
    print("\nNIM tidak ditemukan!")
