import re
class Mean(object):
	media = None
	#
	def __init__(self):
		self.media=0
	def calculateMean(self, array):
		print len(array)
		for x in array:
			numberStr=str(x)
			if numberStr.isdigit():
				self.media=self.media+x
			else:
				self.media=0
				break
		self.media=self.media/len(array)
		return self.media
	


