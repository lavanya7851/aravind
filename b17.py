s=int(input())
sum=0
a=s
while s>0:
	c=s%10
	sum=sum+c*c*c
	s=s//10
if a==sum:
	print("yes")
else:
	print("no")
