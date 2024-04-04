s1=input()

s2=input()

l=[]

for i in range(len(s1)-len(s2)+1):

    if set(s1[i:i+len(s2)])==set(s2):

        l.append(i)

print(l)
