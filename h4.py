n = int(input())
m = [int(x) for x in input().split()[:n]]
for j in m:
    if(m.count(j)==1):
        print(j,end=" ")
