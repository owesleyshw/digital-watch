"""
Requisitos para o código funcionar:

- instalar a biblioteca Tkinter
sudo apt install python3-tk

Developed by Wesley Júnior
"""
from tkinter import *
import tkinter
from datetime import datetime

cor_back = '#0A2E36'
cor_font = '#27FB6B'

def watch():
	time = datetime.now()
	hour = time.strftime("%H:%M:%S")
	day_week = time.strftime("%A")
	day = time.day
	mounth = time.strftime("%b")
	year = time.strftime("%Y")
	
	lbl1.config(text=hour)
	lbl1.after(250, watch)
	lbl2.config(text=str(day_week) + "  " + str(day) + "/" + str(mounth) + "/" + str(year))	

if __name__ == '__main__':
	jan = Tk()
	jan.title("Relógio Digital")
	jan.geometry("520x180")
	jan.resizable(width=FALSE, height=FALSE)
	jan.configure(bg=cor_back)
	frame = Frame(jan)
	lbl1 = Label(frame,text="", font=("Arial 40"), bg=cor_back, fg=cor_font)
	lbl1.pack(fill=X)
	lbl2 = Label(frame, text="", font=("Arial 18"), bg=cor_back, fg=cor_font)
	lbl2.pack(fill=X)
	frame.pack(anchor=CENTER, expand=1)

	watch()
	jan.mainloop()
