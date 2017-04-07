from Figures import Figura
class Cuadrado(Figura):
	def __init__(self,nombre,perimetro,area,lado):
		super().__init__(nombre,perimetro,area)
		self.nombre = nombre
		self.perimetro = perimetro
		self.area = area
		self.lado = lado

	def calc_area(self):
		return self.lado*self.lado

	def calc_perimetro(self):
		return self.lado*4

if __name__ == '__main__':
	cuadrado1 =Cuadrado("Cuadrado",1,5,9)
	print(cuadrado1.getNombre())
	print("Tengo un area y perimetro de: ")
	print(cuadrado1.calc_area()) 
	print(cuadrado1.calc_perimetro())