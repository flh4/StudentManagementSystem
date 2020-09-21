class Student:
	def __init__(self, fname="", lname=""):
		self.fname = fname
		self.lname = lname
		self.address = ''
		self.status = ''
		self.phone = ''
		self.id = ''
		self.advisor = ''
		self.medications = []
		self.courses = []
		self.grades = {'HW':[], 'tests':[], 'quizes':[]}
		
	def setFname(self,name):
		self.fname = name

	def setLname(self,name):
		self.lname = name

	def setAddress(self, add):
		self.address = add

	def setStatus(self, stat):
		self.status = stat 

	def setPhone(self, ph):
		self.phone = ph 

	def setId(self, iD):
		self.id = iD

	def setAdvisor(self, adv):
		self.advisor = adv

	def getFname(self):
		return self.fname

	def getlname(self):
		return self.lname
	
	def getFullName(self):
		return self.fname+' '+self.lname

	def getAddress(self):
		return self.address

	def getStatus(self):
		return self.status

	def getCourses(self):
		return self.courses

	def getGrades(self, x):
		return self.grades[x][0][1]

	def getMedications(self):
		return self.medications 

	def addCourse(self, course):
		self.courses.append(course)

	def addGrade(self, c, grade):
		self.grades[c].append(grade)

	def addMedication(self, med):
		self.medications.append(med)

	def removeCourse(self):
		pass




