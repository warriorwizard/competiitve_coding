wor=input()
t=0
pos_a=ord('a')
pos_z=ord('z')
poz=ord('a')




for i in wor:
	a=ord(i)
	b=abs(a-poz)
	poz=a
	if b>13:
		b=26-b
	t+=b
print(t)
