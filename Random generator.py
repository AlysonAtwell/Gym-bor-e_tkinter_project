from tkinter import * 
from random import randint
root = Tk() # initialize tkinter 
root.title( "Random workout")
root.geometry("600x600")

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