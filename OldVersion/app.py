from student import Student 
import os
from datetime import datetime
import pickle
import time
try:
    # Import for Python2
    import Tkinter as tk
except ImportError:
    # Import for Python3
    import tkinter as tk

class App():
	def __init__(self, parent):
		#Initialize variables
		self.parent = parent
		self.HEIGHT = 700
		self.WIDTH = 800
		self.date = datetime.now().strftime("%B %d %Y")
		self.importData()
		#Set Canvas
		self.canvas = tk.Canvas(self.parent, height=self.HEIGHT, width=self.WIDTH).pack()
		#Initialize Widgets
		self.makeFrames()
		self.makeLabels()
		self.makeButtons()
		self.makeEntry_Fields()
		self.makeMenus()
		self.makeText_Boxes()

	def importData(self):
		try:
			pickle_off2 = open("names.pickle", "rb")
			self.names = pickle.load(pickle_off2)
		except:
			self.names = []
		if not self.names:
			self.names = ['STUDENTS']
			self.students = []
		else:
			pickle_off = open("students.pickle","rb")
			self.students = pickle.load(pickle_off)

	def clear(self):
		self.texxt.delete(0.0, tk.END)
		self.f_name.delete(0, tk.END)
		self.l_name.delete(0, tk.END)

	def fullName(self, f, l):
		return f + ' ' + l

	def write_to_txt(self):
		with open("output.txt", "w") as text_file:
			text_file.write('Name: ')
			text_file.write(self.f_name.get())
			text_file.write(' '+self.l_name.get())
			text_file.write('\n'+self.dob.get())

	def generateReport(self):
		self.texxt.insert(tk.END,"Date:   " + self.date)
		self.texxt.insert(tk.END, "\nName:  "+ self.f_name.get()+' '+self.l_name.get())
		self.texxt.insert(tk.END, "\nId:       "+ self.iD.get())

	def createNewStudent(self):
		self.name = self.fullName(self.f_name.get(), self.l_name.get())
		if self.name not in self.names and self.name != ' ':
			self.s = Student()
			self.s.setfname(self.f_name.get())
			self.s.setlname(self.l_name.get())
			self.students.append(self.s)
			self.updateOptionsMenu()
			self.Save(self.students, "students")
			self.Save(self.names, "names")
			self.clear()
			self.texxt.insert(tk.END, "Student added.")
		elif self.name == ' ':
			print("Fields are empty.")
		else:
			print("Student already exists.")
	
	def updateOptionsMenu(self):
		menu = self.w["menu"]
		for s in self.students:
			self.name = self.fullName(s.getfname(), s.getlname())
			if self.name in self.names:
				pass
			else:
				menu.add_command(label=self.name, command=lambda value=self.name: self.w_variable.set(value))
				self.names.append(self.name)
				print(self.names)
				
	def Save(self, dat, name):
		pickling_on = open(name+".pickle","wb")
		pickle.dump(dat, pickling_on)
		pickling_on.close()
		
	def delStudent(self):
		pass

	def birthdayLetter(self, lst):
		for p in lst:
			if self.emp.getbday() == datetime.now().strftime("%B %d %Y"):
				with open("bday.txt", "w") as f:
					f.write("Happy Birthday "+self.f_name.get()+' '+self.l_name.get())
			else:
				pass

	def makeFrames(self):
		#data entry frame
		self.frame = tk.Frame(self.parent, bg='gray')
		self.frame.place(relx=0, rely=.15, relwidth=.3, relheight=.65)

		#Top frame
		self.frame1 = tk.Frame(self.parent, bg='#004080')
		self.frame1.place(relx=0, rely=0, relwidth=1, relheight=.15)

		#Text Box frame
		self.frame2 = tk.Frame(self.parent)
		self.frame2.place(relx=0, rely=.8, relwidth=.3, relheight=.3)

		#Main Frame
		self.frame3 = tk.Frame(self.parent)
		self.frame3.place(relx=.3, rely=.15, relwidth=.7, relheight=.75)

		#bottom frame
		self.frame4 = tk.Frame(self.parent, bg='#004080')
		self.frame4.place(relx=.3, rely=.9, relwidth=.7, relheight=.1)

	def makeLabels(self):
		#Labels
		self.top_l = tk.Label(self.frame1, text="WELCOME", font=("Helvetica", 40), bg='#004080', fg='#ffb366')
		self.top_l.place(relx=.25, rely=.03, relwidth=.5, relheight=.4)
		self.time_label = tk.Label(self.frame1, text=self.date, font=20, fg='#ffb366', bg='#004080')
		self.time_label.place(relx=.35, rely=.6, relwidth=.3, relheight=.2)
		self.l_f = tk.Label(self.frame, text='Data Entry', font=18, bg='gray')
		self.l_f.place(relx=.35, rely=0, relwidth=.3, relheight=.1)
		self.l1 = tk.Label(self.frame, text='First Name', bg='#d9d9d9', bd=3)
		self.l1.place(relx=0, rely=.1, relwidth=.329, relheight=.04)
		self.l2 = tk.Label(self.frame, text='Last Name', bg='#d9d9d9', bd=3)
		self.l2.place(relx=0, rely=.15, relwidth=.329, relheight=.04)
		self.l3 = tk.Label(self.frame, text='D.O.B.', bg='#d9d9d9', bd=3)
		self.l3.place(relx=0, rely=.2, relwidth=.329, relheight=.04)
		self.l4 = tk.Label(self.frame, text='Age', bg='#d9d9d9', bd=3)
		self.l4.place(relx=0, rely=.25, relwidth=.329, relheight=.04)
		self.l5 = tk.Label(self.frame, text='Phone Num.', bg='#d9d9d9', bd=3)
		self.l5.place(relx=0, rely=.3, relwidth=.329, relheight=.04)
		self.l6 = tk.Label(self.frame, text='I.D.', bg='#d9d9d9', bd=3)
		self.l6.place(relx=0, rely=.35, relwidth=.329, relheight=.04)
		self.l7 = tk.Label(self.frame, text='E-Mail', bg='#d9d9d9', bd=3)
		self.l7.place(relx=0, rely=.4, relwidth=.329, relheight=.04)
		self.l8 = tk.Label(self.frame, text='label', bg='#d9d9d9', bd=3)
		self.l8.place(relx=0, rely=.45, relwidth=.329, relheight=.04)
		self.l9 = tk.Label(self.frame, text='label', bg='#d9d9d9', bd=3)
		self.l9.place(relx=0, rely=.5, relwidth=.329, relheight=.04)
		self.l10 = tk.Label(self.frame, text='label', bg='#d9d9d9', bd=3)
		self.l10.place(relx=0, rely=.55, relwidth=.329, relheight=.04)
		self.l11 = tk.Label(self.frame, text='label', bg='#d9d9d9', bd=3)
		self.l11.place(relx=0, rely=.6, relwidth=.329, relheight=.04)
		self.l12 = tk.Label(self.frame, text='label', bg='#d9d9d9', bd=3)
		self.l12.place(relx=0, rely=.65, relwidth=.329, relheight=.04)

	def makeButtons(self):
		#Buttons
		self.write = tk.Button(self.frame, text="Write .txt", command= self.write_to_txt)
		self.write.place(relx=0, rely=.8, relwidth=.25, relheight=.05)
		self.gen = tk.Button(self.frame, text="Generate", command= self.generateReport)
		self.gen.place(relx=.25, rely=.8, relwidth=.25, relheight=.05)
		self.save = tk.Button(self.frame, text="SAVE", bg='#ff9f80', command = self.createNewStudent)
		self.save.place(relx=.5, rely=.8, relwidth=.25, relheight=.05)
		self.birthday = tk.Button(self.frame, text="birthday", command=lambda: birthdayLetter(students))
		self.birthday.place(relx=0, rely=.85, relwidth=.25, relheight=.05)
		self.btn2 = tk.Button(self.frame, text="Print", command= lambda: print(self.names))
		self.btn2.place(relx=.25, rely=.85, relwidth=.25, relheight=.05)
		self.btn3 = tk.Button(self.frame, text="Delete", command= self.delStudent)
		self.btn3.place(relx=.5, rely=.85, relwidth=.25, relheight=.05)
		self.clr = tk.Button(self.frame, text="CLEAR", bg='yellow', command = self.clear)
		self.clr.place(relx=.75, rely=.8, relwidth=.25, relheight=.2)
		self.quit = tk.Button(self.frame4, text="Quit", bg='red', command=self.parent.quit)
		self.quit.place(relx=.9, rely=.5, relwidth=.1, relheight=.5)

	def makeMenus(self):
		#Drop down menu
		self.w_variable = tk.StringVar(self.parent)
		self.w_variable.set(self.names[0]) # default value
		self.w = tk.OptionMenu(self.frame1, self.w_variable, *self.names)
		self.w.place(relx=0, rely=0, relwidth=.2, relheight=.25)	

	def makeEntry_Fields(self):
		#Entry
		self.f_name = tk.Entry(self.frame, bd=3)
		self.f_name.place(relx=.35, rely=.1, relwidth=.62, relheight=.05)
		self.l_name = tk.Entry(self.frame, bd=3)
		self.l_name.place(relx=.35, rely=.15, relwidth=.62, relheight=.05)
		self.dob = tk.Entry(self.frame, bd=3)
		self.dob.place(relx=.35, rely=.2, relwidth=.62, relheight=.05)
		self.age = tk.Entry(self.frame, bd=3)
		self.age.place(relx=.35, rely=.25, relwidth=.62, relheight=.05)
		self.phone = tk.Entry(self.frame, bd=3)
		self.phone.place(relx=.35, rely=.3, relwidth=.62, relheight=.05)
		self.iD = tk.Entry(self.frame, bd=3)
		self.iD.place(relx=.35, rely=.35, relwidth=.62, relheight=.05)
		self.email = tk.Entry(self.frame, bd=3)
		self.email.place(relx=.35, rely=.4, relwidth=.62, relheight=.05)
		self.address = tk.Entry(self.frame, bd=3)
		self.address.place(relx=.35, rely=.45, relwidth=.62, relheight=.05)
		self.entry9 = tk.Entry(self.frame, bd=3)
		self.entry9.place(relx=.35, rely=.5, relwidth=.62, relheight=.05)
		self.entry10 = tk.Entry(self.frame, bd=3)
		self.entry10.place(relx=.35, rely=.55, relwidth=.62, relheight=.05)
		self.entry11 = tk.Entry(self.frame, bd=3)
		self.entry11.place(relx=.35, rely=.6, relwidth=.62, relheight=.05)
		self.entry12 = tk.Entry(self.frame, bd=3)
		self.entry12.place(relx=.35, rely=.65, relwidth=.62, relheight=.05)

	def makeText_Boxes(self):
		#Output Text Box
		self.texxt = tk.Text(self.frame2, bg='#ffe6cc', font=("Helvetica", 9), fg='red')
		self.texxt.place(relwidth=1, relheight=1)