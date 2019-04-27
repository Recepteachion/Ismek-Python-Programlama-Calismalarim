dizi=input("Kelime veya cümle girin:    ")
if len(dizi)==0 or dizi.isspace():
    print("")
else:
    metin=list(dizi)
    bas=0
    son=0
while True:
    if bas!=0 and son != 0:
        print("".join(metin))
        break
    else:
        if bas==0 and ord(metin[0])<33 or ord(metin[0])==127:
            metin.pop(0)
            if ord(metin[0])>32 and ord(metin[0])!=127:
                bas=1
        if son==0 and ord(metin[-1])<33 or ord(metin[-1])==127:
            metin.pop(-1)
            if ord(metin[-1])>32 and ord(metin[-1])!=127:
                son=1

