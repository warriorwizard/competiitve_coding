def checker(a,b):
	result = min(a, b)
	while result:
		if a % result == 0 and b % result == 0:
			break
		result -= 1
	lcm=int((a*b)/result)
	return result==lcm

n=int(input())
for _ in range(n):
	a=int(input())
	lis=list(map(int,input().split()))
	count=0
	for i in range(len(lis)-1):
		for j in range(i+1,len(lis)):
			a=checker(lis[i],lis[j])
			if a==True:
				count+=1
	print(count)
			
	


