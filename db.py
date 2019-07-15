import pymysql.cursors

with open('server.txt') as f:
    server = f.read().splitlines()

db = pymysql.connect(host=server[0],
			user=server[1],
			password=server[2],
			db =server[3])
cursor = db.cursor()

def getStudents():
	s = []
	cursor.execute("SELECT * FROM student")
	d = cursor.fetchall()
	for i in d:
		s.append(str(i[1]) + ' ' + str(i[2]))
	return s

def getFaculty():
	f = []
	cursor.execute("SELECT * FROM faculty")
	d = cursor.fetchall()
	for i in d:
		f.append(str(i[1]) + ' ' + str(i[2]))
	return f

def addFaculty(idd, f, l, dept, title, pswd):
	query = "INSERT INTO FACULTY VALUES (idd, f, l, dept, title, pswd)"

def DelFaculty():
	pass

def addStudent():
	pass
	#query = "INSERT INTO STUDENT VALUES ()"

def delStudent():
	pass

def getUserPasswd(user):
	query = "SELECT passwd FROM faculty WHERE lname= '%s'"
	try:
		cursor.execute(query % user)
		p = cursor.fetchall()
		return p[0][0]
	except:
		print("Error")

def close_db():
	db.close()



