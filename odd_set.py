t=int(input())

for i in range(t):
	even=0
	odd=0
	n=int(input())
	a=map(int,input().split())
	for i in a:
		if i%2==0:
			even+=1
		else:
			odd+=1
	if even==n and odd==n:
		print('Yes')
	else:
		print('No')
		