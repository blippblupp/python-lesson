jenisSepeda = int(input("Jenis sepeda (1=Biasa, 2=Listrik): "))

if jenisSepeda == 1:
    lamaPenyewaan = int(input("Lama penyewaan: "))
    if lamaPenyewaan > 5: 
        biaya = (lamaPenyewaan - 1) * 5000 + 10000
        diskon = biaya * 0.1
    elif lamaPenyewaan >= 1:
        biaya = (lamaPenyewaan - 1) * 5000 + 10000
        diskon = 0

        print("\nTotal biaya: Rp", biaya)
        print("Diakon: Rp", diskon)
        print("Todal bayar: Rp", biaya - diskon)
    
    else:
        print("Lama penyewaan tidak valid!")

elif jenisSepeda == 2:
    lamaPenyewaan = int(input("Lama penyewaan: "))
    if lamaPenyewaan > 5: 
        biaya = (lamaPenyewaan - 1) * 10000 + 20000
        diskon = biaya * 0.1
    elif lamaPenyewaan >= 1:
        biaya = (lamaPenyewaan - 1) * 10000 + 20000
        diskon = 0
    else:
        print("Lama penyewaan tidak valid!")


    print("\nTotal biaya: Rp", biaya)
    print("Diakon: Rp", diskon)
    print("Todal bayar: Rp", biaya - diskon)

else:
    print("Jenis sepeda tidak valid!")
