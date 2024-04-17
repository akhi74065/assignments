l=list(map(int,input().split()))
p=[]
for i in l:
    for j in l[(l.index(i)+1):]:
        p.append(j-i)
print(max(p))
