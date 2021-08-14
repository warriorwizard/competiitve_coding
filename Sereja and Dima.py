n=int(input())
ser=0
dom=0

a=list(map(int,input().split()))
while len(a)>0:
	if len(a)==1 and n%2!=0:
		ser+=a[0]
		a.pop(0)
	else:
		b=max(a[0],a[-1])
		ser+=b
		a.pop(a.index(b))
		b=max(a[0],a[-1])
		dom+=b
		a.pop(a.index(b))
print(ser)
print(dom)
 