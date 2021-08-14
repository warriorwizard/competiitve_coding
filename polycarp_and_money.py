n=int(input())
for i in range(n):
	a=int(input())
	if a%3==0:
		print(f'{a//3} {a//3}')
	if a%3==1:
		print(f'{a//3+1} {a//3}')
	if a%3==2:
		print(f'{a//3} {a//3+1}')
	
	
