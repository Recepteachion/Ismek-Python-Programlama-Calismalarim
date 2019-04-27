yukseklik =int(input("Lütfen çam ağacı yüksekliğini giriniz: "))
agac_boyu =yukseklik

if 4 <= yukseklik <=20:
    for i in range(1,2*yukseklik+1,2):
        print(' '*yukseklik+i*'*')
        yukseklik-=1
        
    if agac_boyu%2==0:
        for i in range(1,round(agac_boyu/2)+1):
            for j in range(1,2):
                print(" "*(agac_boyu-1)+"| |")
                
    else:
        for i in range(1,round(agac_boyu/2)+2):
            for j in range(1,2):
                print(" "*(agac_boyu-1)+"| |")
                
    print("="*((2*agac_boyu)+1))
    
else:
    print("Yanlış sayı girdiniz.4-20 arasi bir sayi girin.")
