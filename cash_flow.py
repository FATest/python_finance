import numpy as np
from short_rate import *

class Cash_flow(object):
	'''Class model to cash flow series.

	Parameters
	==========
	name : string
		name of the object

	time_list : list/array-like
		list of (positive) year fractions

	cash_flows: list/array-like
		list of cash flow values

	short_rate: instance of short_rate class
		short rate object used for discounting

	Methods
	=======
	presentValue :
		returns an array with present value
	netPresentValue :
		return NPV for cash flow series
	'''

	def __init__(self, name, time_list,cash_flows,short_rate):
		self.name = name
		self.time_list = time_list
		self.cash_flows = cash_flows
		self.short_rate = short_rate

	def presentValue(self):
		df = self.short_rate.getDiscountFactors(self.time_list)
		return np.array(self.cash_flows)*df
	
	def netPresentValue(self):
		return np.sum(self.presentValue())

sr = Short_rate('r',0.5)

time_list = [0,1,2,]
cash_flows = [-100,50,75]
cfs = Cash_flow('cfs',time_list,cash_flows,sr)

print cfs.netPresentValue()