from Figures import Figura
class Circulo(Figura):
	def __init__(self,nombre,perimetro,area,radio):
		super().__init__(nombre,perimetro,area)
		self.nombre = nombre
		self.perimetro = perimetro
		self.area = area
		self.radio = radio

	def calc_area(self,radio):
		return self.radio*self.radio*3.1416

	def calc_perimetro(self):
		return "Como se sacaba? xD"
	
if __name__ == '__main__':
	c1 = Circulo("Circulo",2,5,9)
	print(c1.getNombre())
	print("Tengo un area y perimetro de: ")
	print(c1.calc_area(1)) 
	print(c1.calc_perimetro())