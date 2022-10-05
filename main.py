from tkinter import * 

root = Tk() # initialize thinker 
#from PIL import ImageTK, Image 


#root.iconbitmap('E:\Fitness for anyone.png')

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



btn=Button(root, text="Open Window", command = openwindow)
btn.pack(padx=20, pady=20)

Button(root,text= "Close Openend Window", command=lambda: new_window.destroy()).pack()

root.geometry("925x500+300+200")#Set the geometry of frame
root.title("Main_window")# Title of Application
root.configure(bg="#fff")
root.resizable(False,False) # can not be resizing window

#img = PhotoImage(file="E:\Fitness for anyone.png") #logo image

 #Label(root,image=img, bg= 'white'.place(x=50, y=50))

frame= Frame(root, width=350, height=350, bg="red")
frame.place(x=480, y=70)

heading =Label(frame,text='Sign in', fg ='57a1f8',bg = 'white', font = ("Helvetica", 23, 'bold') )
heading.place(x=100,y=5)    

def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    if code.get()=='':
        code.insert(0,'Password')
                       
code = Entry(frame,width=25,fg='black', border=0,bg='white', font = ('Helvetica', 11,))
code.place(x=30, y=150)
code.insert(0,'Password')
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25, y=17)

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
root.geometry("400x400")
chair_warmup=["Neck Stretch","Knee Lifts","Sit and Stand","Heel Slides","Tummy Twists for Abs","Seated Jumping Jacks","Seated Forward Bend","Knee to Chest","Ankle Rotations","Bicep curls with Resistance Bands"]

def pick():
    warmups = ["Heel Touch", "Squats", "Toe Taps","Arm Circles: to release tension in your shoulders","Overhead arm reaches: the best exercise to kickstart energy and muscle warmth","Hip Rotations: ideal for loosening your lower body","Side knee lifts: the best exercise for strengthening your core","Squat with arm lift: for an entire body burn","Squat with reaches: to fire up your glutes","Lunges: to warmup your thighs","Push-ups: for an all-over arm burn","Jumping Jacks: to increase blood flow and loosen your entire body","Plank Walk Outs: to engage your core, hamstrings, and shoulders","High Knees: get your blood pumping and activates the muscles","Jumping Rope: maximize your heart rate"]
    
    #convert to a set
    warmups_set = set(warmups)
    
    #Convert back to list
    unique_warmups= list(warmups_set)
    
    # create our list size variable 
    our_number = len(unique_warmups) - 1
    
    # create a random number between 0 and 5 
    rando = randint(0, our_number )
    #winnerLabel= Label(root,text=len(entries), font=("Helvetica", 18)) previously needed to get the winner
    winnerLabel= Label(root,text=unique_warmups[rando], font=("Helvetica", 18))
    winnerLabel.pack(pady=50)

topLabel = Label(root, text="LET'S GET STARTED!", font=("Helvetica",24))
topLabel.pack(pady=20)

winButton = Button(root, text="Pick Your Warm UP!!", font=("Helvetica",24), command = pick)
winButton.pack(pady=20)
root.mainloop()