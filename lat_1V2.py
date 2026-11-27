nilai = [90, 75, 21, 22, 30]


def tukar(asal, tujuan):
    nilai[asal], nilai[tujuan] = nilai[tujuan], nilai[asal]
    return nilai

tukar(3, 4)
print(nilai)