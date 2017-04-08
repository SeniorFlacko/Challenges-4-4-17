import random
class Horse:
	def __init__(self,name,step,recorrido):
		self.name = name
		self.step = step
		self.recorrido = recorrido

	def gallop(self):
		self.step = random.randint(1, 5)
		self.recorrido += self.step
		print(self.recorrido)
		return self.step


if __name__ == '__main__':
	c1 = Horse("Caballo1",0,0)
	c2 = Horse("Caballo2",0,0)
	
	while c1.recorrido<20 and c2.recorrido<20:
		c1.gallop()
		c2.gallop()

	print("El recorrido total del c1: ")
	print(c1.recorrido)
	print("El recorrido total del c2: ")
	print(c2.recorrido)

	
	if c1.recorrido>=20 and c2.recorrido>=20:
		print("Empate")
	elif c1.recorrido > c2.recorrido:
		print("C1 gano")
	else:
		print("C2 gano")
	
	
