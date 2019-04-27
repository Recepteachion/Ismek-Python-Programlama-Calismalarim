import random

bilmeceler =[
    ['Türkiye\'nin u\'su en çok olan şehri neresidir?', 'bolu'],
    ['Pazardan aldım 1 tane eve geldim 1000 tane', 'nar'],
    ['Sıra sıra odalar birbirini kovalar', 'tren'],
    ['Bin ilik bin düğüm bin diyesin bilmeyesin', 'ağ'],
    ['Kanadı var kuş değil, kuyruğu var at değil', 'balık'],
    ['Düşünen file ne denir?', 'filozof'],
    ['Tavuklar en çok hangi ülkeyi sever?', 'mısır'],
    ['Ben giderim o gider, ben dururum o durur', 'gölge'],
    ['İp bağladım sıpaya uçtu gitti tepeye', 'uçurtma'],
    ['Çilek ek almadığında ne olur?', 'çilli']
]

puan=0

while len(bilmeceler) > 0:
    soruNo     =random.randint(0,len(bilmeceler)-1)
    soru       =bilmeceler[soruNo][0]
    dogruCevap =bilmeceler[soruNo][1]
    cevap      =input(soru+" > ").lower()

    if len(cevap) > 0:
        if cevap == dogruCevap:
            print("Doğru bildiniz.")
            puan+=1
        else:
            print("Yanlış yazdınız.Cevap: ",dogruCevap)
        bilmeceler.pop(soruNo)
    else:
        break
print("Puanınız: ",puan)
            
    

    
