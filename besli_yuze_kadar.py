print(*range(0,101,5))

print([*range(0,101,5)])

print([i for i in range(101) if i%5==0])

for i in range(1,101,5):
    print(i,end="-")

for i in range(101):
    if i%5==0:
        print(i,end="-")
