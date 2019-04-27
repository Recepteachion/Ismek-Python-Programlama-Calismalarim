import random

devam="e"
while devam=="e":
    sayi=random.randint(1,500)
    print(sayi)
    sayac=0
    print("1 ile 500 arasında bir sayı tuttum")
    while True:
        cevap=int(input("Tahmin et > "))
        sayac+=1
        if cevap==sayi:
            print("%d tahminde buldun"%sayac)
            if sayac == 1:
                print("Aklımı mı  okudun ilk tahminde buldun.")
            elif sayac < 5:
                print("Bravo",sayac,"tahminde bildin.")
            elif sayac < 10:
                print("10'dan az tahminde bildin.")
            else:
                print("Biraz zor oldu ama %d tahminde buldun."%sayac)
            break
        elif cevap < sayi:
            print("Tuttuğum sayı daha büyük.")
        else:
            print("Tuttuğum sayı daha küçük.")
    devam=input("Tekrar oynamak ister misiniz (e,h)?").lower()
print("Benimle oynadığın için teşekkür ederim.\nİyi günler dilerim.")
                      
                
