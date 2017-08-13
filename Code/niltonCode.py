import math
class CodeDeviation(object):
	def __init__(self):
		self.standardDeviation=0
	def calcularDesviacion(self,numero, n):
		esNegativo=False
		resultado=None
		if type(numero) == long or type(numero) == int or type(numero) == float:
			if numero < 0:
				esNegativo = True
			else:
				esNegativo = False
				if n > 1:
					numero = (numero) / (n - 1)
					resultado = math.sqrt(numero)
		return  resultado

		