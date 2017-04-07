class Figura:

	def __init__(self,nombre,perimetro,area):
		self.nombre = nombre
		self.perimetro = perimetro
		self.area = area

	def getNombre(self):
		return "Me llamo %s" % self.nombre

	def setArea(self,area):
		self.area=area

	def getArea(self):
		return self.area

	def setPerimetro(self,perimetro):
		self.perimetro=perimetro

	def getPerimetro(self):
		return self.perimetro

	def calc_area(self):
		pass

	def calc_perimetro(self):
		pass
		
if __name__ == '__main__':
	f1 = Figura("Cuadrado",10,19)
	f1.setPerimetro(21)
	print(f1.getNombre())
	