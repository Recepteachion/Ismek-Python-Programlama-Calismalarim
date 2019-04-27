#-*- coding:utf-8 -*-
alt=1
ust=5
sayac=1
print("*"*32,"ÇARPIM TABLOSU","*"*32,"\n")

while sayac < 3: #2 satır olacağından burası 3
    for i in range(1,11):
        for j in range(1,11):
            if alt <= j <= ust:
                if j == 5 or j == 10:
                    print("%d  x  %2d = %2d"%(j,i,i*j))
                else:
                    print("%d  x  %2d =%2d\t\t"%(j,i,i*j))
            else:
                continue
    sayac+=1
    print("\r")
    alt=6
    ust=10
                    
            
