from tkinter import *
from PIL import ImageTk, Image


root = Tk() 
#root.iconbitmap("E:\Gym-bor-e_tkinter_project\images\4042280_dumbell_gym_healthy life_take exercise_training_icon.png")
#root.iconphoto(True, root)

new_window =""
def openwindow():
    global new_window
    new_window = Toplevel(root)
    new_window.geometry("250x250")
    new_window.title("New Window")
    new_window.resizable(False, False) # can not be resizing window.
    lbl = Label(new_window, text="I am the new window")
    lbl.pack()
    btn2 =Button(new_window, text="Close Me", command=lambda: new_window.destroy())
    btn2.pack()


#Registration for new users
btn=Button(root, text="Open Window", command = openwindow)
btn.pack(padx=20, pady=20)

Button(root,text= "Close Openend Window", command=lambda: new_window.destroy()).pack()

root.geometry("925x500+300+200")#Set the geometry of frame
root.title("Main_window")# Title of Application
root.configure(bg="#fff")
root.resizable(False,False) # can not be resizing window

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

Frame(frame,width=295,height=2,bg='black').place(x=25, y=107)

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
         
Frame(frame,width=295,height=2,bg='black').place(x=25, y=177)  

###Confirm Code--------------------------------                                                         
def on_enter(e):
    confirm_code.delete(0,'end')
def on_leave(e):
    if confirm_code.get()=='':
       confirm_code.insert,(0,'Confirm_Password')

                       
confirm_code = Entry(frame,width=25,fg='black', border=0,bg='white', font=('Helvetica',11))
confirm_code.place(x=30, y=150)
confirm_code.insert(0,'Password')
confirm_code.bind("<FocusIn>", on_enter)
confirm_code.bind("<FocusOut>", on_leave)
         
Frame(frame,width=295,height=2,bg='black').place(x=25, y=247) 
###--------------------------------------------------------------
Button(frame, text="Sign up", width=39, pady=7, bg="blue", fg= "white", border=0).place(x=35, y=280) 
label=Label(frame, text="I have an account", fg = 'black', bg = 'white', cursor='hand2', font=('Helvetica',9))
label.place(x=90,y=340)

sign_In_btn=Button(root, text="Sign In", command=openwindow, width=39, pady=7, border=0, bg="white", cursor='hand2', fg="blue")
btn.pack(padx=20, pady=20)

sign_Up_btn=Button(root, text="Sign Up", command=openwindow, width=39, pady=7, border=0, bg="white", cursor='hand2', fg="blue")
btn.pack(padx=20, pady=20)




#show window 
root.mainloop()