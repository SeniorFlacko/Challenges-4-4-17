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

def shortestChainLen(start,target,d):
	item = [start,1]
	Q = deque('')
	



