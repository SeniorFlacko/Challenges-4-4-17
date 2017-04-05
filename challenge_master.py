from collections import deque
def isadjacent(palabra1,palabra2):
	count=0
	n=len(palabra1)
	for i in range(n):
		if palabra1[i] is not palabra2[i]:
			count+=1
		if count>1:
			return False
	return True if count is 1 else False

d = ["hot", "dot", "dog", "lot", "log", "cog"]
start  = "hit"
target = "cog"

Q = deque('')
Q.append(start)
cont=1

while Q:
	curr = Q.popleft()
	for j in d:
		if isadjacent(curr,j):
			cont+=1
			Q.append(j)
			print(Q)
			d.remove(j)
			print(d)
			if j is target:
				print("Ya encontre el target")
				print(cont)



	



