nilai = [90, 75, 21, 22, 30]

i = 0
while i in range(len(nilai) - 1):
    if nilai[i] > nilai[i + 1]:
        nilai2 = nilai[i]
        nilai[i] = nilai[i + 1]
        nilai[i + 1] = nilai2
    i += 1

i = 0
while i in range(len(nilai) - 1):
    if nilai[i] > nilai[i + 1]:
        nilai2 = nilai[i]
        nilai[i] = nilai[i + 1]
        nilai[i + 1] = nilai2
    i += 1



print(nilai)
print("V1")