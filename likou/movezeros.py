num=[0,1,3,5,0]
j=0
for i in range(len(num)):
    if num[i]!=0:
        num[j]=num[i]
        if i!=j:
            num[i]=0
        j=j+1
print(num)
