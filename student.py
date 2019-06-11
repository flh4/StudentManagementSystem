class Student:
	def __init__(self, fname="", lname=""):
		self.fname = fname
		self.lname = lname
		self.courses = []
		self.grades = {'HW':[], 'tests':[]}
		
	def setfname(self,name):
		self.fname = name

	def setlname(self,name):
		self.lname = name

	def getfname(self):
		return self.fname

	def getlname(self):
		return self.lname
	
	def fullname(self):
		return self.fname+' '+self.lname

	def addHWgrade(self, grade):
		self.grades['HW'].append(grade)

	def getGrades(self):
		return self.grades 
