class Student:
	def __init__(self, fname="", lname=""):
		self.fname = fname
		self.lname = lname
		
	def setfname(self,name):
		self.fname = name

	def setlname(self,name):
		self.lname = name

	def getfname(self):
		return self.fname

	def getlname(self):
		return self.lname

