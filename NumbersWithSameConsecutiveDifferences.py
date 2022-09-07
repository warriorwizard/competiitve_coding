from collections import deque
n=3
k=7
def diff(n,k):
	ans=[]
	d=deque((1,d) for d in range(1,10))
	#print(d)
	while d:
		pos,num=d.pop()
		#print(num)
		#print(pos)
		if pos==n:
			ans.append(num)
		else:
			for j in range(10):
				if abs(num%10-j)==k:
					d.append((pos+1,num*10+j))
					print((pos+1,num*10+j))
			
	#print(ans)
		
		
		
		
diff(n,k)