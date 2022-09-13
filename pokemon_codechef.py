from collections import Counter
n=int(input())
for _ in range(n):
	a=int(input())
	lis=[]
	cout=1
	land=list(map(int,input().split()))
	water=list(map(int,input().split()))
	final=[]
	for i in range(a):
		count=0
		for j in range(a):
			if land[i]>land[j] or water[i]>water[j]:
				count+=1
		lis.append(count)
	
	ma=max(lis)
	print(lis.count(ma))
	
