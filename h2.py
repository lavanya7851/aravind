ch = int(input())
s = list(map(int,input().split()))
s.sort(reverse=True)
j=0
for i in range(0,len(s)):
	j=(j*10)+s[i]
print(j)
