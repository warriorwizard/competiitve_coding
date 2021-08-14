n,t=map(int,input().split())
a=10**(n-1)+1
b=10**n
for i in range(a,b):
	if i%t==0:
		print(i)
		break
else:
	print(-1)