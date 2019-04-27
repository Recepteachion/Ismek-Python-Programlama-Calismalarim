def cevir(lst):
    sayilar=lst.split(',')
    #return list(map(lambda x: int(x),sayilar))
    sayilar2=[]
    for i in sayilar:
        sayilar2.append(int(i))
    return sayilar2
def toplam(lst):
    t=0
    for i in cevir(lst):
        t+=i
    return t
def carpim(lst):
    c=1
    for i in cevir(lst):
        c*=i
    return c
def ortalama(lst):
    listem=cevir(lst)
    return toplam(lst)/len(listem)
def standartSapma(lst):
    ort=ortalama(lst)
    topla=0
    liste=cevir(lst)
    for k in liste:
        topla+=(k-ort)**2
    return (topla/(len(liste)-1))**0.5
if __name__=="__main__":
    liste=input("Sayıları aralarına virgül koyarak yazın.\nSayılar: ")
    print("Girdiğiniz sayıların toplamı")
    print(*cevir(liste),sep="+",end=" ")
    print("=",toplam(liste))
    print("Girdiğiniz sayıların çarpımı")
    print(*cevir(liste),sep="x",end=" ")
    print("=",carpim(liste))
    print("Girdiğiniz sayıların ortalaması")
    print(*cevir(liste),sep=",",end=" ")
    print("= %.2f"%ortalama(liste))
    print("Girdiğiniz sayıların standart sapması")
    print(*cevir(liste),sep=" ",end=" ")
    print("= %.4f"%standartSapma(liste))
