n=int(input())
a=list(map(int,input().split()))
t=int(input())
for i in range(t):
	x,y=map(int,input().split())
	if x==n:
		pass
	else:
		a[x]+=(a[x-1]-y)
	if x==1:
		pass
	else:
		a[x-2]+=y-1
	a[x-1]-=(a[x-1]-y+1)
	a[x-1]-=y-1
for i in a:
	print(i)
 