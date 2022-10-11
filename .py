from tkinter import *
from PIL import ImageTk, Image

#Photo
root = Tk() 
#root.iconbitmap("E:\Gym-bor-e_tkinter_project\images\4042280_dumbell_gym_healthy life_take exercise_training_icon.png")
#root.iconphoto(True, root)

####-Login setup--------
root.geometry("925x500+300+200")#Set the geometry of frame
root.title("Main_window")# Title of Application
root.configure(bg="#E4F7FF")
root.resizable(False,False) # can not be resizing window

def sign():
    username=user.get()
    password=code.get()
    
    if username=='admin' and password=='1234':
            screen=Toplevel(root)
            screen.title("BAB")
            screen. geometry("925x500+300+200")
            screen.configure(bg="#E4F7FF")

           
            
            
#img = PhotoImage("E:\Gym-bor-e_tkinter_project\images\4042280_dumbell_gym_healthy life_take exercise_training_icon.png") #logo image
#Label(root,image=img, bg= 'white'.place(x=50, y=50))

frame= Frame(root, width=350, height=390, bg="#fff") # Square that holds the sign in sign,username & password
frame.place(x=480, y=70)

heading =Label(frame,text='Sign in', fg ='blue',bg ='white', font = ("Helvetica", 23, 'bold') ) # SIGN IN LOGO WORDS
heading.place(x=100,y=5)    

###
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    if user.get()=='':
        user.insert(0,'Username')
                       
user = Entry(frame,width=25,fg='black', border=0,bg='white', font = ('Helvetica', 11,))
user.place(x=30, y=80)
user.insert(0,'Username')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25, y=107) #line 

###Password Entry ------------------------------------------
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    if code.get()=='':
        code.insert,(0,'Password')

                       
code = Entry(frame,width=25,fg='black', border=0,bg='white', font=('Helvetica',11))
code.place(x=30, y=150)
code.insert(0,'Password')
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)
         
Frame(frame,width=295,height=2,bg='black').place(x=25, y=177) #Line 

###Confirm Code--------------------------------                                                         
def on_enter(e):
    confirm_code.delete(0,'end')
def on_leave(e):
    if confirm_code.get()=='':
       confirm_code.insert,(0,'Confirm_Password')

                       
confirm_code = Entry(frame,width=25,fg='black', border=0,bg='white', font=('Helvetica',11))
confirm_code.place(x=30, y=220)
confirm_code.insert(0,'Confirm Password')
confirm_code.bind("<FocusIn>", on_enter)
confirm_code.bind("<FocusOut>", on_leave)
         
Frame(frame,width=295,height=2,bg='black').place(x=25, y=247) 
###--------------------------------------------------------------
Button(frame, text="Sign up", width=39, pady=7, bg="blue", fg= "white", border=0).place(x=35, y=280) 
label=Label(frame, text="I have an account", fg = 'black', bg = 'white', cursor='hand2', font=('Helvetica',9))
label.place(x=90,y=340)

sign_In=Button(frame, text="Sign In", width=6, border=0, bg="white", cursor='hand2', fg="blue")
sign_In.place(x=200, y= 340)






#show window 
root.mainloop()