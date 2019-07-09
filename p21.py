nu1=input().split()
nu2=input().split()
nu3=input().split()
if(nu1[0]==nu2[0]==nu3[0] or nu1[1]==nu2[1]==nu3[1] or (nu1[0]==nu1[1] and nu2[0]==nu2[1] and nu3[0]==nu3[1])):
    print('yes')
else:
    print('no')
