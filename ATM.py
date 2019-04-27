menu="""
-------------------
1.Para Çekme
2.Para Yatırma 
3.Hesap Bilgisi
4.Kart İade
-------------------
Yapmak istediğiniz işlemi seçin ==> """
hesap=1000
limit=-500
likit=500
def para_cekme():
    global hesap
    giris=int(input("Ne kadar para çekmek istersiniz? > "))
    if limit < hesap-giris:
        hesap=hesap-giris
        print("Hesabınızda",hesap,"TL kalmıştır.")
    elif hesap-giris<0:
        a=abs(limit)
        a-=giris
        print(limit,"limitinizden",a,"TL paranız kalmıştır.")

    else:
        print("Hesabınızdaki para yetersiz.")
        alt_sorgu()

def para_yatirma():
    global hesap
    giris=int(input("Yatırmak istediğini para miktarını giriniz: "))
    hesap=hesap+giris
    print("Hesabınızda",hesap,"TL kadar paranız vardır.")
    alt_sorgu()

def hesap_bilgisi():
    global hesap
    print("Hesabınızda",hesap,"TL kalmıştır.")
    alt_sorgu()

def kart_iade():
    print("İyi günler diler. Yine bekleriz.")

def alt_sorgu():
    soru=int(input("Ana menüye dönmek için 1'e,Çıkış yapmak için 2'ye basınız: "))
    if soru==1:
        menu
    elif soru==2:
        kart_iade()
    else:
        print("Yanlış bir tuşa bastınız")
        alt_sorgu()

if __name__=="__main__":
     while True:
        islem = int(input(menu))
        if islem==1:
            para_cekme()
        elif islem==2:
            para_yatirma()
        elif islem==3:
            hesap_bilgisi()
        else :
            kart_iade()
            break

