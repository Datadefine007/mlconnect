a=[23232,32,3232,32,313,213213,1,434,324324,324324]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]==a[j],a[i]
print(a)
a1=a[0]
for k in range(len(a)):
    if a[k]>a1:
        a1=a[k]
print(a1)


x=8
a=0
b=1
d=[]
while x<8:
    d.append(x)
    c=a+b
    b=c
    
    c=a

print(d)