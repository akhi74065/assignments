l=list(map(int,input().split()))
max1=0
max2=0
for i in l:
    if i>max1:
        max2=max1
        max1=i
print(max2)