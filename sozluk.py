sozluk ={
    "tr-en":{   # sozluk["tr-en"][kelime]
        "elma":"apple",
        "asker": "soldier",
        "meyve" : "fruit",
        "günaydın": "good morning",
        "araba":"car"
    },
    "en-tr":{   # sozluk["en-tr"][word]
        "computer":"bilgisayar",
        "phone":"telefon",
        "monitor":"ekran",
        "food":"yemek",
        "student":"öğrenci"
    }
}

menu="""-----SÖZLÜK PROGRAMI------
    1. Turkce - İngilizce
    2. English - Turkish
    3. Çıkış ( Quit)
        Seçiminiz : """
#print(sozluk["en-tr"])
while True:
    secim=input(menu)
    if secim=="3":
        print("Programdan çıkılıyor.\n İyi günler diler yine bekleriz. ")
        break
    elif secim=="1":
        while True:
            kelime=input("Kelimeyi girin:   ")
            klm=sozluk["tr-en"].get(kelime,"Aradığınız kelime sözlükte yok. ")
            if len(kelime)==0:
                break
            else:
                print(klm)
    elif secim=="2":
        while True:
            word=input("Entry word: ")
            wrd=sozluk["en-tr"].get(word,"The word is not in dictionary.")
            if len(word)==0:
                break
            else:
                print(wrd)
    else:
        print("Yanlış bir seçenek girdiniz.\nTekrar deneyin")





















