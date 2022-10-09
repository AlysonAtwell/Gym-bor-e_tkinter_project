from tkinter import * #Import the required Library
from random import randint
from tracemalloc import start
from turtle import right
from PIL import ImageTk 
from tkinter import messagebox

root = Tk() # initialize tkinter 
root.title( "Random workout")# Title of Application
root.geometry("925x500+300+200")#Set the geometry of frame
#ICONPHOTO
#root.iconbitmap("E:\Master  Files for GUI APP\photos for gui\Fitness for anyone.png")
root.configure(bg="#E4F7FF")
root.resizable(False,False) # can not be resizing window
x= IntVar() #is the radio button to function 
    
def order():
    if (x.get()==0):
        return pick1
    
    elif (x.get()==1):
        return pick2
    elif (x.get()==2):
        return pick3
    else:
        print('Pick a position to do warm-ups') # maybe place button  
      
'''
y= IntVar() # initialize y value which are the picks for the radiobutton to link to button in new window pick button   
    
def warm():
    if (Y.get()==0):
        return pick1
    elif (Y.get()==1):
        return pick2
    elif (Y.get()==2):
        return pick3
    else:
        print('Pick a position to do warm-ups') # maybe place button 

variable=y, # groups pick 1, pick2, pick 3 together if they share the same v
'''
chair_workout =""
def openwindow():
    global chair_workout
    chair_workout = Toplevel(root)
    chair_workout.geometry("925x500+300+200")#Set the geometry of the window
    chair_workout.title("Chair Warm-up")
    chair_workout.configure(bg="#E4F7FF")
    chair_workout.resizable(False, False) # can not be resizing window.
    lbl = Label(chair_workout, text="Congratulations, here's your workout!",font=("Helvetica",30),bg="#E4F7FF", fg= "blue",).pack(pady=18) #label at top of window
    btn2 =Button(chair_workout, text="Close Me",pady=7,padx=20, bg="#E4F7FF", fg= "blue", border=0, command=lambda: chair_workout.destroy()).pack(anchor=E) # Button to New warm up window
    pickButton = Button(chair_workout, text="Start Your Warm UP!!", font=("Helvetica",24),fg= "blue", bg="#E4F7FF", command = pick1) # Start Your Warm UP
    pickButton.pack()
    
floor_workout =""
def openwindow():
    global floor_workout
    floor_workout = Toplevel(root)
    floor_workout.geometry("925x500+300+200")#Set the geometry of the window
    floor_workout.title("Floor Warm-up")
    floor_workout.configure(bg="#E4F7FF")
    floor_workout.resizable(False, False) # can not be resizing window.
    lbl = Label(floor_workout, text="Congratulations, here's your workout!",font=("Helvetica",30),bg="#E4F7FF", fg= "blue",).pack(pady=18) #label at top of window
    btn2 =Button(floor_workout, text="Close Me",pady=7,padx=20, bg="#E4F7FF", fg= "blue", border=0, command=lambda: floor_workout.destroy()).pack(anchor=E) # Button to New warm up window
    pickButton = Button(floor_workout, text="Start Your Warm UP!!", font=("Helvetica",24),fg= "blue", bg="#E4F7FF", command = pick3) # Start Your Warm UP
    pickButton.pack()
    
stand_workout =""
def openwindow():
    global stand_workout
    stand_workout = Toplevel(root)
    stand_workout.geometry("925x500+300+200")#Set the geometry of the window
    stand_workout.title("Stand Warm-up")
    stand_workout.configure(bg="#E4F7FF")
    stand_workout.resizable(False, False) # can not be resizing window.
    lbl = Label(stand_workout, text="Congratulations, here's your workout!",font=("Helvetica",30),bg="#E4F7FF", fg= "blue",).pack(pady=18) #label at top of window
    btn2 =Button(stand_workout, text="Close Me",pady=7,padx=20, bg="#E4F7FF", fg= "blue", border=0, command=lambda: stand_workout.destroy()).pack(anchor=E) # Button to New warm up window
    pickButton = Button(stand_workout, text="Start Your Warm UP!!", font=("Helvetica",24),fg= "blue", bg="#E4F7FF", command = pick2) # Start Your Warm UP
    pickButton.pack()
    
    
def open_window(self):
       chair_workout = chair_workout(self)
       chair_workout.grab_set()  
        
def open_window(self):
       stand_workout = stand_workout(self)
       stand_workout.grab_set() 
       
def open_window(self):
       floor_workout = floor_workout(self)
       floor_workout.grab_set()        
        
        
x= IntVar() #is the radio button to function 
    
def order():
    if (x.get()==0):
        return pick1
    elif (x.get()==1):
        return pick2()
    elif (x.get()==2):
        return pick3()
    else:
        print('Pick a position to do warm-ups') # maybe place button  
      
       
               

def pick1():
    warmups = ["Neck Stretch","Knee Lifts","Sit and Stand","Heel Slides","Tummy Twists for Abs","Seated Jumping Jacks","Seated Forward Bend",
               "Knee to Chest","Ankle Rotations","Bicep curls with Resistance Bands"]
    warmups_set = set(warmups)#takes list and convert to a set
    unique_warmups= list(warmups_set)#Convert back to list
    our_number = len(unique_warmups) - 1 # create our list size variable 
    rando = randint(0, our_number ) # create a random number between 0 and 5 
    winnerLabel= Label(chair_workout,text=len(warmups), font=("Helvetica", 18)) #previously needed to get the winner
    pick1_Label= Label(chair_workout,text=unique_warmups[rando], font=("Comic Sans MS", 18),fg ="blue", bg="#E4F7FF")
    pick1_Label.pack(pady=10)

def pick2():
    warmups = ["Knee Lifts","Sit and Stand","Squats","Arm Circles: to release tension in your shoulders",
               "Overhead arm reaches: the best exercise to kickstart energy and muscle warmth","Hip Rotations: ideal for loosening your lower body",
               "Side knee lifts: the best exercise for strengthening your core","Squat with arm lift: for an entire body burn",
               "Squat with reaches: to fire up your glutes","Lunges: to warmup your thighs","Jumping Jacks: to increase blood flow and loosen your entire body",
               "Plank Walk Outs: to engage your core, hamstrings, and shoulders","High Knees: get your blood pumping and activates the muscles",
               "Jumping Rope: maximize your heart rate","Knee Lifts", "Stand and Sit", "squat"]
    warmups_set = set(warmups)#convert to a set
    unique_warmups= list(warmups_set)#Convert back to list
    our_number = len(unique_warmups) - 1 # create our list size variable 
    rando = randint(0, our_number ) # create a random number between 0 and 5 
    winnerLabel= Label(root,text=len(warmups), font=("Helvetica", 18)) #previously needed to get the winner
    pick2Label= Label(stand_workout,text=unique_warmups[rando], font=("Comic Sans MS", 18),fg ="blue", bg="#E4F7FF")
    pick2Label.pack(pady=10)

def pick3():
    warmups = ["Knee to Chest","dead bug","Heel Touch", "Toe Taps","Overhead arm reaches: the best exercise to kickstart energy and muscle warmth",
               "Push-ups: for an all-over arm burn","Snow Angels: to increase blood flow and loosen your entire body",
               "Plank Walk Outs: to engage your core, hamstrings, and shoulders","High Knees: get your blood pumping and activates the muscles",
               "Hug knees to chest"]
    warmups_set = set(warmups)#convert to a set
    unique_warmups= list(warmups_set)#Convert back to list
    our_number = len(unique_warmups) - 1 # create our list size variable 
    rando = randint(0, our_number ) # create a random number between 0 and 5 
    #winnerLabel= Label(root,text=len(warmups), font=("Helvetica", 18)) #previously needed to get the winner
    pick3Label= Label(floor_workout,text=unique_warmups[rando], font=("Comic Sans MS", 18),fg ="blue", bg="#E4F7FF")
    pick3Label.pack(pady=10)
    
       
#Labels For 1st Page  
welLabel = Label(root, text="Welcome to GYMBORE!", fg ="blue", bg="#E4F7FF", font=("Helvetica",30)) #Welcom Label Header label 
welLabel.pack(pady=20)

greetLabel = Label(root, text="Ready to Start Warm Up...", fg ="blue", bg="#E4F7FF", font=("Helvetica",15)) #Welcom Label Header label 
greetLabel.pack(pady=10)

topLabel = Label(root, text="Now Pick Location", fg ="blue", bg="#E4F7FF", font=("Helvetica",10)) #Header label 
topLabel.pack(pady=10)
#Instructions


def clicker():
    global pop
    Pop = Toplevel(root)
    Pop.title("Gymbore Instructions")
    pop.geometry=("300x300")
    pop.configure(bg="#E4F7FF")
    pop_Label = Label(root, text="Instructions", fg ="blue", bg="#E4F7FF", font=("Helvetica",10)) #Instructions label 
    pop_Label.pack(pady=10)
    pop_btn=Button(root,text="Instructions",pady=7,padx=20, bg="#E4F7FF", fg= "blue", border=0, command=lambda: pop.destroy()).pack(anchor=NE) # Button to New warm up window
    my_frame= Frame= Frame(pop, bg="#E4F7FF")
    my_frame.pack(pady=5)
    
clik_button=Button(root, text="Instructions",padx=5, bg="#E4F7FF", fg= "blue", border=0)
clik_button.pack(anchor=NE)
#clk_label=Label(root,text="Instructions",pady=7,padx=20, bg="#E4F7FF", fg= "blue", border=0)
#clk_label.pack()
    
#radio button
def new_func():
    x= IntVar()
    return x

x = new_func()

choose_workout = ['Chair', 'Stand', 'Floor']

for index in range(len(choose_workout)):
    radiobutton = Radiobutton(root, 
                              text=choose_workout[index], # adds text to radio
                              variable=x, # groups radio together if they share the same v
                              value=index, #assigns each radio button a different value
                              padx =25,
                              font= ("Helvetica",15),
                              # image = positionimages[index], #image to radio button
                              fg ="blue", bg="#E4F7FF", #font & background color
                              compound = 'left', #adds image & text to left of text
                              indicatoron=0, #eliminate circle indicatoron
                              width = 15, #sets the width of the button)
                              command = order # set command of radio button to function
                                )
    radiobutton.pack()

btn=Button(root, text="Go to Workout",font = ("Helvetica",25), width=39, pady=7, bg="#E4F7FF", fg= "blue", border=0, command = openwindow) # was open window not go to workout
btn.pack(padx=20, pady=20)

Button(root,text="Close Warm UP Window",pady=7,padx=20, bg="#E4F7FF", fg= "blue", border=0, command=lambda: stand_workout.destroy()).pack(anchor=E) # Button to New warm up window


root.mainloop() # must have to display window  
