def ss(a,b):
  if(len(a)==len(b)):
    return("yes")
  else:
   return("no")
a,b=map(str,input().split())
print(ss(a,b))
