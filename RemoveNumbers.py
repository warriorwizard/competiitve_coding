n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
# 1 want to minimize | even 0
# 2 wants to maximize| odd 1

for i in range(len(b)):
	if i%2==0:
		bi=b[i]
		evensum=0
		oddsum=0
		for i in a:
			if i%bi==0:
				evensum+=i
			else:
				oddsum+=i
		print(evensum)
		print(oddsum)
		if evensum>oddsum:
			for i in a:
				if i%bi==0:
					a.remove(i)
		else:
			for i in a:
				if i%bi!=0:
					a.remove(i)
	else:
		bi=b[i]
		evensum=0
		oddsum=0
		for i in a:
			if i%bi==0:
				evensum+=i
			else:
				oddsum+=i
		if oddsum>=evensum:
			for i in a:
				if i%bi==0:
					a.remove(i)
		else:
			for i in a:
				if i%bi!=0:
					a.remove(i)
print(a)
		
