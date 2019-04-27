fobiNaci=int(input("Kaç tane fobiNaci sayısı istiyorsunuz(5-100): "))
fobi=[1,1]

for i in range(fobiNaci+1):
    fobi.append(fobi[-1]+fobi[-2])

if 5 <= i <=100:
    print("Buyrun fobinacci sayılarınız > \n",fobi)
else:
    print("Aralıktaki kadar yardımcı olabilirim.")
