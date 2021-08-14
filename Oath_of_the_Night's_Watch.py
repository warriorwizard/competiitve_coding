n=int(input())
a=list(map(int,input().split()))
b=min(a)
c=max(a)
len=0
for i in a:
	if i<c and i>b:
		len+=1
print(len)	