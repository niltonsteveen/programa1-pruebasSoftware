import math
class CodeDeviation(object):
	def __init__(self):
		self.standardDeviation=0
	def calcularDesviacion(self,numero, n):
		esNegativo=False
		resultado=None
		if type(numero) == int or type(numero) == float:
			if numero < 0:
				esNegativo = True
			else:
				esNegativo = False
				if n > 1:
					numero = (numero) / (n - 1)
					resultado = math.sqrt(numero)
		return  resultado

	def calcularNumerador(self,muestra):
		resultado=0
		media=45
		for numero in muestra:
			if type(numero) == int or type(numero) == float:
				resultado = resultado + math.pow((numero - media), 2)
			else:
				resultado=0
				break
		return resultado


		