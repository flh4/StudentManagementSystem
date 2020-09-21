from app import App
try:
    # Import for Python2
    import Tkinter as tk
except ImportError:
    # Import for Python3
    import tkinter as tk


if __name__ == '__main__':
	window = tk.Tk()
	App(window)
	window.mainloop()