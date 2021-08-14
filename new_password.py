a,b=map(int,input().split())
d=ord('a')
c=[]
for i in range(b):
	c.append(chr(d+1))
	d+=1
print(c)
e=a-b
f=[]
if e>0:
	pass