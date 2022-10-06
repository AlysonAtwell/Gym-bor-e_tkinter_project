from tkinter import * 
from random import randint
from turtle import right


root = Tk() # initialize tkinter 
root.title( "Random workout")# Title of Application
root.geometry("925x500+300+200")#Set the geometry of frame
#ICONPHOTO
root.configure(bg="#E4F7FF")
root.resizable(False,False) # can not be resizing window

new_window =""
def openwindow():
    global new_window
    new_window = Toplevel(root)
    new_window.geometry("925x500+300+200")
    new_window.title("New Warm-up")
    new_window.configure(bg="#E4F7FF")
    new_window.resizable(False, False) # can not be resizing window.
    lbl = Label(new_window, text="Congratulations, here's your workout!",font=("Helvetica",30),bg="#E4F7FF", fg= "blue",)
    lbl.pack(pady=18)
    btn2 =Button(new_window, text="Close Me",pady=7,padx=20, bg="#E4F7FF", fg= "blue", border=0, command=lambda: new_window.destroy()).pack(anchor=E) # Button to New warm up window
    winButton = Button(new_window, text="Start Your Warm UP!!", font=("Helvetica",24),fg= "blue", bg="#E4F7FF", command = pick)
    winButton.pack()




#having trouble installing images #Radio buttons to choose workout
#standimage = PhotoImage(file="E:\Gym-bor-e_tkinter_project\photos for gui\chair.png") #
#floorimage = PhotoImage(file="E:\Gym-bor-e_tkinter_project\photos for gui\exercises.png") #
#positionimages= ["chairimage","standimage',"floorimage"] # Position for exercise

chair=["Neck Stretch","Knee Lifts","Sit and Stand","Heel Slides","Tummy Twists for Abs","Seated Jumping Jacks","Seated Forward Bend","Knee to Chest","Ankle Rotations","Bicep curls with Resistance Bands"]
stand=["Knee Lifts","Sit and Stand","Squats","Arm Circles: to release tension in your shoulders","Overhead arm reaches: the best exercise to kickstart energy and muscle warmth","Hip Rotations: ideal for loosening your lower body","Side knee lifts: the best exercise for strengthening your core","Squat with arm lift: for an entire body burn","Squat with reaches: to fire up your glutes","Lunges: to warmup your thighs","Jumping Jacks: to increase blood flow and loosen your entire body","Plank Walk Outs: to engage your core, hamstrings, and shoulders","High Knees: get your blood pumping and activates the muscles","Jumping Rope: maximize your heart rate","Knee Lifts", "Stand and Sit", "squat"]
floor=["Knee to Chest","dead bug","Heel Touch", "Toe Taps","Overhead arm reaches: the best exercise to kickstart energy and muscle warmth","Push-ups: for an all-over arm burn","Snow Angels: to increase blood flow and loosen your entire body","Plank Walk Outs: to engage your core, hamstrings, and shoulders","High Knees: get your blood pumping and activates the muscles","Hug knees to chest"]

def order():
    if (x.get()==0):
        chair.get()
    elif (x.get()==1):
        stand.get() 
    elif (x.get()==2):
        floor.get()
    else:
        print('Pick a location to do Warm-ups') # maybe place button
        

def pick():
    warmups = ["Heel Touch", "Squats", "Toe Taps","Arm Circles: to release tension in your shoulders","Overhead arm reaches: the best exercise to kickstart energy and muscle warmth","Hip Rotations: ideal for loosening your lower body","Side knee lifts: the best exercise for strengthening your core","Squat with arm lift: for an entire body burn","Squat with reaches: to fire up your glutes","Lunges: to warmup your thighs","Push-ups: for an all-over arm burn","Jumping Jacks: to increase blood flow and loosen your entire body","Plank Walk Outs: to engage your core, hamstrings, and shoulders","High Knees: get your blood pumping and activates the muscles","Jumping Rope: maximize your heart rate"]
    warmups_set = set(warmups)#convert to a set
    unique_warmups= list(warmups_set)#Convert back to list
    our_number = len(unique_warmups) - 1 # create our list size variable 
    rando = randint(0, our_number ) # create a random number between 0 and 5 
    #winnerLabel= Label(root,text=len(entries), font=("Helvetica", 18)) previously needed to get the winner
    winnerLabel= Label(new_window,text=unique_warmups[rando], font=("Comic Sans MS", 18),fg ="blue", bg="#E4F7FF")
    winnerLabel.pack(pady=10)
    
welLabel = Label(root, text="Welcome!", fg ="blue", bg="#E4F7FF", font=("Helvetica",30)) #Welcom Label Header label 
welLabel.pack(pady=20)

greetLabel = Label(root, text="Ready to Start Warm Up...", fg ="blue", bg="#E4F7FF", font=("Helvetica",25)) #Welcom Label Header label 
greetLabel.pack(pady=10)

topLabel = Label(root, text="Now Pick Location", fg ="blue", bg="#E4F7FF", font=("Helvetica",20)) #Header label 
topLabel.pack(pady=10)


x= IntVar()

choose_workout = ['chair', 'stand', 'floor']

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



Button(root,text="Close Warm UP Window",pady=7,padx=20, bg="#E4F7FF", fg= "blue", border=0, command=lambda: new_window.destroy()).pack(anchor=E) # Button to New warm up window



root.mainloop()