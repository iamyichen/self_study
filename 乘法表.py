l=[{"{1}x{0}".format(i,j):i*j for j in range(1,i+1)} for i in range(1,10)]
for item in l:
    for k,v in item.items():
        print("{}={}".format(k,v),end=" ")
    print()