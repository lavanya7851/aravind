n = int(input())
m = [int(x) for x in input().split()[:n]]
o = []
for i in range(0,int(len(m))):
    if(i==m[i]):
        o.append(i)
if(int(len(o)))!=0:
    for u in o:
        print(u,end=" ")
else:
    print(-1)
