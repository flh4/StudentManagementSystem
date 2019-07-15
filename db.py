import pymysql.cursors


db = pymysql.connect(host='localhost',
						user='rick',
						password='Drab$$Wymoop2$',
						db ='school')
cursor = db.cursor()


def getStudents():
	s = []
	cursor.execute("SELECT * FROM faculty")
	d = cursor.fetchall()
	for i in d:
		s.append(str(i[1]) + ' ' + str(i[2]))
	return s

def addFaculty(idd, f, l, dept, title, pswd):
	query = "INSERT INTO FACULTY VALUES (idd, f, l, dept, title, pswd)"

def getUserPasswd(user):
	query = "SELECT passwd FROM faculty WHERE lname= '%s'"
	try:
		cursor.execute(query % user)
		p = cursor.fetchall()
		return p[0][0]
	except:
		print("Error")

def addStudent():
	pass

def delStudent():
	pass


#db.close()



