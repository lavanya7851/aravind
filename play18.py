nc=int(input())
c=0
for i in range(0,nc):
    s=str(input())
    if(sorted(s)==sorted("kabali")):
        c=c+1
print(c)
