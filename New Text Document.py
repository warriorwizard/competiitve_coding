k,r=map(int,input().split())
n=1
while True:
	if (k*n)%10==0:
		print(n)
		break
	elif ((k*n)-r)%10==0:
		print(n)
		break
	n+=1