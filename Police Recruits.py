n=int(input())
t=0
a=list(map(int,input().split()))
temp=0
for i in range(n):
	if a[i]<0 and temp==0:
		t+=1
	elif a[i]<0 and temp!=0:
		temp+=a[i]
	elif a[i]>0:
		temp+=a[i]

print(t)