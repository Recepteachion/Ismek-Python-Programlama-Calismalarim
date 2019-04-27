asallar   =[]
lasalar   =[]
sayi      = 1
sayac     = 0

num=int(input("Kaç tane asal sayıda bulalım: "))

while sayac < num:
    sayi += 1
    for i in range(2,sayi):
        if (sayi%i) == 0:
            break
    else:
        asallar.append(sayi)
        sayac += 1

print(asallar)
print(len(asallar))

for s in asallar:
    tersi =0
    sa = s
    while s > 0:
        tersi=tersi*10+s%10
        s//=10
    if tersi in asallar and sa != tersi:
        lasalar.append(sa)
print(lasalar)
print(len(lasalar))

