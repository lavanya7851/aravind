nc=str(input())
s={}

for i in nc:
    if i not in s.keys():
        s[i]=nc.count(i)
print(max(s, key=s.get))
