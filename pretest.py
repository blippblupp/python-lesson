nama = []
nim = []
nilai = []
jumlahMahasiswa = 2
i = 0
nilaiMax = 0
nilaiMin = 100
total = 0

print("Masukan data anda:")
while(i<jumlahMahasiswa):
    inpNama = input("Maskan nama: ")
    inpNim = input("Masukan nim: ")
    inpNilai = int(input("Masukan nilai: "))
    print("-------------------------")
    nama.append(inpNama)
    nim.append(inpNim)
    nilai.append(inpNilai)

    # mencari juara
    if (nilaiMax<nilai[i]):
        indexMax=i
        nilaiMax=nilai[i]

    # total
    total = total + nilai[i]

    # nilai terkecil
    if (nilaiMin>nilai[i]):
        nilaiMin=nilai[i]

        i+=1

print("-------------------------")
print("Data mahasiswa juara")
print("Nama", nama[indexMax])
print("NIM", nim[indexMax])
print("Nilai", nilai[indexMax])
print("-------------------------")
print("Nilai rata-rata = ", total/jumlahMahasiswa)
print("-------------------------")
print("Nilai terkecil = ", nilaiMin)