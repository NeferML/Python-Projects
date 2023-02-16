from tkinter import *
from tkinter import ttk
import datetime

#GUI object
root = Tk()
root.title('Alarm clock')

#Window parameters
mainFrame = ttk.Frame(root, padding="3 3 12 12")
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

currentTime = datetime.date.today()

ttk.Label(mainFrame, text=f"{currentTime}"). grid(column=2, row=2, sticky=W)

root.mainloop()

