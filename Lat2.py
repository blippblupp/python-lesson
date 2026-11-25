
log_suhu = [27, 29, 31, 28, 32, 34, 29, 33]
batas_suhu = 30

hasil = -1

for i in range(len(log_suhu) - 1):
    if log_suhu[i] > batas_suhu and log_suhu[i + 1] > batas_suhu:
        hasil = i
        break

print(hasil)
