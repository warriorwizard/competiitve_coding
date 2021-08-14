n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)):
	print(a.index(i+1)+1,end=' ')
