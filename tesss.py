nim = []
nilaiTugas = []
uts = []
uas = []
mahasiswa = 2
nilaiAkhir = []
nilaiMax = 0
i = 0

while i < mahasiswa:
    inpNim = input("Masukan nim: ")
    inpNilaitugas = float(input("Masukan nilai tugas: "))
    inpUts = float(input("Masukan nilai uts: "))
    inpUas = float(input("Masukan nilai uas: "))
    print("-------------------------")
    nim.append(inpNim)
    nilaiTugas.append(inpNilaitugas)
    uts.append(inpUts)
    uas.append(inpUas)

    nilaiAkhir[i] = (0.3 * inpNilaitugas) + (0.3 * inpUts) + (0.4 * inpUas)
    nilaiAkhir.append(nilaiAkhir)

    #if nilai<nilaiMax:

    
    i += 1

print("Nim:", nim)
print("Nilai akhir:", nilaiAkhir)

