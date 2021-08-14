t=int(input())
for i in range(t):
	n=int(input())
	a=list(map(int,input().split()))
	for i in a:
		coun=a.count(i)
		if coun==1:
			print(a.index(i)+1)