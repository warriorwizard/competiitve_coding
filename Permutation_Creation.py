a=int(input())
for _ in range(a):
	n=int(input())
	# l1=[]
	# l2=[]
	if n<=3:
		print(-1)
	elif n==4:
		print("3 1 4 2")
	else:
		if n%2!=0:
			l1=[i for i in range(1,(n//2)+2)]
			l2=[i for i in range((n//2+2),n+1)]
			# print(l1)
			# print(l2)
			final=[]
			while l1 and l2:
				final.append(l1.pop(0))
				final.append(l2.pop(0))
			final.append(l1[-1])
			# print(final)
			for i in final:
				print(i,end=" ")
		else:
			l1=[i for i in range(1,(n//2)+1)]
			l2=[i for i in range((n//2+1),n+1)]
			# print(l1)
			# print(l2)
			final=[]
			while l1 and l2:
				final.append(l1.pop(0))
				final.append(l2.pop(0))
			# print(final)
			for i in final:
				print(i,end=" ")
			