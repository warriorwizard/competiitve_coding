#anton  and letters
lis=input().strip('{').strip('}')
a=[]
for i in lis:
	if i.isalpha()==True:
		a.append(i)
print(len(set(a)))
