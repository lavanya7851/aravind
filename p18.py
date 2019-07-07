nc,k=map(int,input().split())
for i in range(max(nc,k),100000):
    if(i%nc==0 and i%k==0):
        print(i)
        break
