import re
class Mean(object):
	media = None
	#
	def __init__(self):
		self.media=0
	def calculateMean(self, array):
		p = re.compile('\d+(\.\d+)?')
		if len(array)>0:
			for x in array:
				if p.match(str(x)) != None:
					self.media=self.media+x
				else:
					self.media=0
					break

			self.media=self.media/len(array)
		return self.media
	


