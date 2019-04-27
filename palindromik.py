kelimeler=[]

while True:
    gir=input("Bir sözcük yazınız: ").lower()
    if len(gir)>0:
        kelimeler.append(gir)
    else:
        break

polindromik=[]
for sozcuk in kelimeler:
    if sozcuk==sozcuk[::-1]:
        polindromik.append(sozcuk)

print("Girdiğiniz {} sözcükten {} tanesi polindromiktir".format(len(kelimeler),len(polindromik)),sorted(polindromik),sep="\n")
