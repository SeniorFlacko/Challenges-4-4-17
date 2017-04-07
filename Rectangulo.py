from Figures import Figura
class Rectangulo(Figura):
	def __init__(self,nombre,perimetro,area,lado1,lado2):
		super().__init__(nombre,perimetro,area)
		self.nombre = nombre
		self.perimetro = perimetro
		self.area = area
		self.lado1 = lado1
		self.lado2 = lado2

	def calc_area(self):
		return self.lado1*self.lado2

	def calc_perimetro(self):
		return (self.lado1*2) + (self.lado2*2)

if __name__ == '__main__':
	r1 =Rectangulo("Rectangulo",1,5,9,10)
	print(r1.getNombre())
	print("Tengo un area y perimetro de: ")
	print(r1.calc_area()) 
	print(r1.calc_perimetro())