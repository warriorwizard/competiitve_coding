players = [1,1,1]
trainers = [10]
players.sort()
trainers.sort()
count=0
while players:
	i=players.pop(0)
	#print(i)
	for j in trainers:
		if i<=j:
			count+=1
			print(trainers.pop(trainers.index(j)))
			break
	
		
print(count)