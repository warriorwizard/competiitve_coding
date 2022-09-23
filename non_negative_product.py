import math
n=int(input())
for _ in range(n):
	no=0
	a=int(input())
	lis=list(map(int,input().split()))
	temp=math.prod(lis)
	if temp<0:
		no+=1
		
	print(no)