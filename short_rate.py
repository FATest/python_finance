import numpy as np

class Short_rate(object):
	'''Class model to a constant short rate object

	Parameters
	==========
	name : string
		name of the object

	rate : float
		positive, constant short rate

	Methods
	=======
	getDiscountFactors :
		returns discount factors for given list/array
		of dates/times (as year fractions)
	'''

	def __init__(self, name, rate):
		self.name = name
		self.rate = rate

	def getDiscountFactors(self,time_list):
		time_list = np.array(time_list)
		return np.exp(-self.rate*time_list)
	
# sr = Short_rate('r',0.05)
# print "{}{}".format(sr.name,sr.getDiscountFactors([0,1,2,]))