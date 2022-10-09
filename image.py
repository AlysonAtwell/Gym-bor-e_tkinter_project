import time
from tkinter import*
from turtle import update
root=Tk() # initialize
import PIL



root.title("Images")






 #Stop Watch since photo will not be visible
def clock ():
        hour = time.strftime('%H')
        minute = time.strftime('%M')
        seconds = time.strftime('%S')
    
0, 0, 0 # setting clock face with variables 
run = False # using a boolen variable 
    
    #Functions
def Start():
        global Runtime 
        if not running:
            update()
            running= True
            

# Showing the time window
stopwatch_label = Label(root(text = "start", height= 2, width= 2, font = "Helvetica",command= stop) #Label to display time
stopwatch_label.pack()

# Button functions
start_button = Button(root, text="pause", height= 2, width= 2, fg ="blue", bg="#E4F7FF", font=("Helvetica",20)command= start) #Header label 
start_button.pack(side = LEFT) # start button 
           
pause_button = Button(root, text="pause", height= 2, width= 2, fg ="blue", bg="#E4F7FF", font=("Helvetica",20)command= pause) #Header label 
pause_button.pack(side = LEFT) # start button

reset_button = Button(root, text='reset', height= 2, width= 2, fg ="blue", bg="#E4F7FF", font=("Helvetica",20), command= reset) #Header label 
reset_button.pack(side = LEFT) #

quit_button = Label(root, text='quit',height= 2, width= 2, fg ="blue", bg="#E4F7FF", font=("Helvetica",20)) #Header label 
quit_button.pack(pady=10)

root.mainloop()