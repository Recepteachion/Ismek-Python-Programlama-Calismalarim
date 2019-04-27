a=1;b=6

for k in range(2):
    for i in range(1,11):
        for j in range(a,b):
            print("   | %2d x %2d = %3d" %(i,j,i*j),end="")
        print("     |")

    if k == 0: a=6;b=11;print()
