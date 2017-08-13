import math
class CodeDeviation(object):
	def __init__(self):
		self.standardDeviation=0
	def calcularDesviacion(self,numero):
		esNegativo=False
		resultado=None
		if numero<0:
			esNegativo=True
		else:
			esNegativo=False
			resultado = math.sqrt(numero)
		return  resultado

		