import numpy as np
from short_rate import *

class Market_environment(object):
	'''Class model a market environment for valuation.

	Attributes
	==========
	name : string
		name of the object

	pricing_date : datetime object
		date of the market environment
	
	Methods
	=======
	
	addConstant: 
		adds a constant

	getConstant: 
		gets a constant

	addList:
		adds a list

	getList:
		gets a list

	addCurve:
		adds a market curve

	getCurve:
		adds a market curve

	addEnvironment:
		adds and overwrites market environments
		with new constants, lists, and curves
	'''

	def __init__(self, name, pricing_date):
		self.name = name
		self.pricing_date = pricing_date
		self.constants = {}
		self.lists = {}
		self.curves = {}

	def addConstant(self,key, constant):
		self.constants[key] = constant
		
	
	def getConstant(self,key):
		return self.constants[key]

	def addList(self,key,list_object):
		self.lists[key] = list_object

	def getList(self,key):
		return self.lists[key]

	def addCurve(self,key, curve):
		self.curves[key] =curve
	
	def getCurve(self,key):
		return self.curves[key]

	def addEnvironment(self,env):
		#overwrite existing values, if they exist

		for key in env.constants:
			self.contants[key] = env.constants[key]

		for key in env.lists:
			self.lists[key] = env.lists[key]

		for key in env.curves:
			self.curves[key] = env.curves[key]
