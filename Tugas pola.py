n = int(input("n = "))   # gunakan bilangan ganjil, misal 9
tengah = n // 2

for i in range(n):
    d = abs(i - tengah)          # jarak baris dari tengah
    baris = ""
    for j in range(n):
        # bintang di sisi kiri dan kanan, bagian tengah dikosongkan
        if j <= d or j >= n - 1 - d:
            baris += "* "
        else:
            baris += "  "
    print(baris)