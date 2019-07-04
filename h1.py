num=int(input())
s=input().split(" ")
final_s=[]
for i in range(0,len(s)):
  for j in range(i+1,len(s)):
    if not(s[j] in final_s):
      if(s[i]==s[j]):
        final_s.append(s[j])
final_s=sorted(final_s)
if(len(final_s)==0):
  print("unique")
else:
  print(" ".join(final_s))
