ogrenciler = [
                ["Selim Taş",85,70,60],
                ["Ayla Yalçın",90,55,70],
                ["Ragıp Arslan",70,80,100],
		["Sema Maraşlı",60,70,80],
		["Hayri Kozalak",80,70,90],
		["Cemil Çelepci",40,30,50],
		["Nur Efşan",60,70,75],
		["Hamit Gül",70,40,90],
		["Rukiye Güleç",60,40,100],
		["Saliha Yıldız",90,80,90]
]

toplam_mat    =0  ; toplam_fen     =0 ; toplam_turkce  =0
endusukmat    =100; enyuksekmat    =0
endusukfen    =100; enyuksekfen    =0
endusukturkce =100; enyuksekturkce =0

for o in ogrenciler:
    toplam_mat += o[1]
    if o[1] > enyuksekmat:
        enyuksekmat = o[1]
    if o[1] < endusukmat:
        endusukmat = o[1]
    toplam_fen += o[2]
    if o[2] > enyuksekfen:
        enyuksekfen=o[2]
    if o[2] < endusukfen:
        endusukfen=o[2]
    toplam_turkce += o[3]
    if o[3] > enyuksekturkce:
        enyuksekturkce = o[3]
    if o[3] < endusukturkce:
        endusukturkce  = o[3]

ortMat   =toplam_mat/len(ogrenciler)
ortFen   =toplam_fen/len(ogrenciler)
ortTurkce=toplam_turkce/len(ogrenciler)

print("Matematik dersinin ortalaması : %.2f" %ortMat)
print("Fen dersinin ortalaması :%.2f" %ortFen)
print("Türkçe dersinin ortalaması:%.2f" %ortTurkce)
print()
matEnYuksekOgrenci    =[]
matEnDusukOgrenci     =[]
fenEnYuksekOgrenci    =[]
fenEnDusukOgrenci     =[]
turkceEnYuksekOgrenci =[]
turkceEnDusukOgrenci  =[]

sayac1=0; sayac2=0; sayac3=0

for ogr in ogrenciler:
    if ogr[1]==enyuksekmat:
        matEnYuksekOgrenci.append(ogr[0])
    if ogr[1]==endusukmat:
        matEnDusukOgrenci.append(ogr[0])
    if ogr[1]>=ortMat:
        sayac1+=1
    if ogr[2]==enyuksekfen:
        fenEnYuksekOgrenci.append(ogr[0])
    if ogr[2]==endusukfen:
        fenEnDusukOgrenci.append(ogr[0])
    if ogr[2] >=ortFen:
        sayac2+=1
    if ogr[3]==enyuksekturkce:
        turkceEnYuksekOgrenci.append(ogr[0])
    if ogr[3]==endusukturkce:
        turkceEnDusukOgrenci.append(ogr[0])
    if ogr[3] >= ortTurkce:
        sayac3+=1
print("Matematik dersindeki en yüksek not:",enyuksekmat,matEnYuksekOgrenci)
print("Matematik dersindeki en düşük not:",endusukmat, matEnDusukOgrenci)
print("%d kişi matematik dersi ortalamasının üstünde"%sayac1)
print()
print("Fen Bilimleri dersindeki en yüksek not:",enyuksekfen,fenEnYuksekOgrenci)
print("Fen bilimleri dersindeki en düşük not:",endusukfen,fenEnDusukOgrenci)
print("%d kişi fen bilimleri dersi ortalamasının üstünde"%sayac2)
print()
print("Türkçe dersindeki en yüksek not:",enyuksekturkce,turkceEnYuksekOgrenci)
print("Türkçe dersindeki en düşük not:",endusukturkce,turkceEnDusukOgrenci)
print("%d kişi türkçe dersi ortalamasının üstünde"%sayac3)



        























    
        
    
