s,v=map(int,(input().split()))
c=0
for x in range(2,v):
        if(s%x==0 and v%x==0):
            c=x
print(c)
