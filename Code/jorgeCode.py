import re
class Mean(object):
	media = None
	#
	def __init__(self):
		self.media=0
	def calculateMean(self, array):
		for x in array:
			numberStr=str(x)
			print numberStr
			if numberStr.isdigit():
				self.media=self.media+x
			else:
				self.media=0
				break
		return self.media
	


