
class Mean(object):
	media = None
	#
	def __init__(self):
		self.media=None
	def calculateMean(self, array):
		for x in array:
			self.media=self.media+x
		return self.media
	


