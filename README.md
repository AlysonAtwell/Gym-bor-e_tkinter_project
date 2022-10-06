# Gym-bor-e_tkinter_project
#Gym*bor*e GUI Documentation#
### By Alyson McHale
10/01/2022
Gym*bor*e is a application to 
**Summary**
Gym*bor*e is an application to randomly pick your warm-up & cool-down exercise. If your tired of the same old routine. Try Gym*br*ee. Mix thing up. We all need to warm up with stretches to warm our body up for the main weightlifting or cardo.This will help you from hurting yourself and with a cool down after. it gives you body an appertunity Gym*br*ee is being developed for my elderly father and my teenage son. 

**Step By Step Coding***
Allowing tkinder to import in to the program
from tkinter import *

instants of tk.class (object)
root=Tk()#makes window

- [x] Two Windows  1. new_window = Toplevel(root)   2.  root=Tk()
  
new_window = Tk.Toplevel(root) #using Toplevel gives options to add more windows
***Toplevel**

Mainloop
root.mainloop()  #required to recieve window

#Size of Window
my_window.geometry("925x500+300+200")
root.title( "Random workout")# Title of Application
root.geometry("925x500+300+200")#Set the geometry of frame
root.configure(bg="#fff") background color
root.resizable(False,False) # can not be resizing window

  