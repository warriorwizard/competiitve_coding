#anton and polyhadrons
#python3

n=int(input())
a=[]
for i in range(n):
	b=input()
	a.append(b)
Tetrahedron=4
Cube=6 
Octahedron=8
Dodecahedron=12
Icosahedron=20
total=0
for i in a:
	if i=='Tetrahedron':
		total+=4
	elif i=="Cube":
		total+=6
	elif i=="Octahedron":
		total+=8
	elif i=="Dodecahedron":
		total+=12
	elif i=='Icosahedron':
		total+=20

print(total)
