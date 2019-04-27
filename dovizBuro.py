doviz = {'$':[4.08,4.10,500],
         '€':[5.05,5.09,1000],
         '£':[5.20,5.25,100],
         'TL':[0,0,5000]}
dovizAdiSozlugu = {1:'$', 2:'€', 3:'£'}
menu1 = """---------------------------
1. Döviz Alış İşlemi
2. Döviz Satış İşlemi
3. Kasa Görüntüle
4. Programdan Çıkış
Seçiminiz    :"""
menu2="""   Döviz Türü
    1. $
    2. €
    3. £
    4. Geri
    Seçiminiz: """
while True:
    sec = int(input(menu1))
    if sec ==1:
        print("-" * 30)
        dovizTuru = int(input(menu2))
        if dovizTuru == 4:
            continue
        islemMiktari = float(input("Kaç %s alacaksınız? "%dovizAdiSozlugu[dovizTuru]))
        odenecekTL = islemMiktari * doviz[dovizAdiSozlugu[dovizTuru]][0]
        if doviz['TL'][2] >= odenecekTL:
            doviz[dovizAdiSozlugu[dovizTuru]][2] += islemMiktari
            print("Ödemeniz gereken tutar %.2f TL"%odenecekTL)
            doviz['TL'][2] -= odenecekTL
        else:
            print("Maalesef o kadar TL yok")

    elif sec == 2:
        dovizTuru = int(input(menu2))
        if dovizTuru == 4:
            continue
        islemMiktari = float(input("Kaç %s vereceksiniz? " % dovizAdiSozlugu[dovizTuru]))
        alinacakTL = islemMiktari * doviz[dovizAdiSozlugu[dovizTuru]][1]
        if doviz[dovizAdiSozlugu[dovizTuru]][2] >= islemMiktari:
            doviz[dovizAdiSozlugu[dovizTuru]][2] -= islemMiktari
            print("Müşteriden alacağınız tutar %.2f TL" % alinacakTL)
            doviz['TL'][2] += alinacakTL
        else:
            print("Maalesef o kadar %s yok" % dovizAdiSozlugu[dovizTuru])
    elif sec == 3:
        for para in doviz:
            print(para, "\t-----\t",doviz[para][2])

    elif sec == 4:
        print("Programdan çıkılıyor")
        break
    else:
        print("Yanlış giriş yaptınız.")