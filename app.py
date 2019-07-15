from db import *
from datetime import datetime
import time
import hashlib
import os
try:
    # Import for Python2
    import Tkinter as tk
    from Tkinter import messagebox
except ImportError:
    # Import for Python3
    import tkinter as tk
    from tkinter import messagebox

class App():
	def __init__(self, parent):
		#Initialize variables
		self.parent = parent
		self.HEIGHT = 500
		self.WIDTH = 600
		self.date = datetime.now().strftime("%B %d, %Y")
		self.students = getStudents()
		#Set Canvas
		self.canvas = tk.Canvas(self.parent, height=self.HEIGHT, width=self.WIDTH).pack()
		#Initialize Widgets
		self.Top()
		self.LoginPage()

	def hashPass(self, p):
		pass

	def unHashPass(self, p):
		pass

	def loginn(self):
		usr = self.user.get()
		pas = self.passwd.get()
		if pas == getUserPasswd(usr):
			self.login.destroy()
			self.initiate_main()
		else:
			self.user.delete(0, 'end')
			self.passwd.delete(0, 'end')
			messagebox.showerror("Error", "Wrong Username or Password")


	def initiate_main(self):
		self.main = tk.Frame(self.parent, bg='gray')
		self.main.place(relx=0, rely=.2, relwidth=1, relheight=.8)
		
	def addFac(self):
		self.login.destroy()
		self.add = tk.Frame(self.parent, bg='blue')
		self.add.place(relx=0, rely=.2, relwidth=1, relheight=.8)
		self.back = tk.Button(self.add, text="Back to Login", command=self.LoginPage)
		self.back.place(relx=0, rely=.85, relwidth=.25, relheight=.15)

	def Top(self):
		#Frame
		self.top = tk.Frame(self.parent, bg='#004080')
		self.top.place(relx=0, rely=0, relwidth=1, relheight=.20)
		#Labels
		self.welcome = tk.Label(self.top, text="AWESOME SMS", font=("Helvetica", 38), bg='#004080', fg='#ffb366')
		self.time_l = tk.Label(self.top, text=self.date, font=20, fg='#ffb366', bg='#004080')
		self.welcome.place(relx=.15, rely=.03, relwidth=.7, relheight=.5)
		self.time_l.place(relx=.35, rely=.6, relwidth=.3, relheight=.2)

	def LoginPage(self):
		#Frame
		self.login = tk.Frame(self.parent, bg='gray')
		self.login.place(relx=0, rely=.2, relwidth=1, relheight=.8)
		
		#Labels
		self.username = tk.Label(self.login, text='User', font=15, fg='#ffb366', bg='gray')
		self.password = tk.Label(self.login, text='Password', font=15, fg='#ffb366', bg='gray')
		self.username.place(relx=.35, rely=.2, relwidth=.3, relheight=.1)
		self.password.place(relx=.35, rely=.4, relwidth=.3, relheight=.1)
		
		#Entries
		self.user = tk.Entry(self.login, bd=3, font='14')
		self.passwd = tk.Entry(self.login, show='*', fg='blue', bd=3, font='14')
		self.user.place(relx=.35, rely=.3, relwidth=.3, relheight=.1)
		self.passwd.place(relx=.35, rely=.5, relwidth=.3, relheight=.1)
		
		#Buttons
		self.submit = tk.Button(self.login, text="Login", font=14, bg='green', command= self.loginn)
		self.quit = tk.Button(self.login, text="Quit", font=14, bg='red', command=self.parent.quit)
		self.add = tk.Button(self.login, text="Add a Faculty Member", bg='orange', command=self.addFac)
		self.submit.place(relx=0, rely=.85, relwidth=.25, relheight=.15)
		self.quit.place(relx=.75, rely=.85, relwidth=.25, relheight=.15)
		self.add.place(relx=.36, rely=0, relwidth=.3, relheight=.1)