from tkinter import *

ws = Tk()
ws.geometry('400x450+1000+300')#Set the geometry of frame
ws.title('PythonGuides: Stopwatch')# Title of the   From PHYTHOM GUIDEs
ws.config(bg='#299617') #background color   
#ws.iconbitmap('stopwatch.ico')# will not work in my applications
ws.resizable(0,0)#resizable determines the amount window that can be stretched by user.
#it accepts x and y value in this case value is 0, 0 that means window can’t be resized.

#Creating Global variables
counter = -1
running = False
def counter_label(lbl):   #the counter_label is accepting the argument label
    def count():   #count() is another function passed in counter_label.
        if running:
            global counter #If we want to use a particular variable in another function, 
                            #then we have to declare that variable as a global variable.
            if counter==-1:             #declared counter & running as a global variable
                display="00"  #  function sets the value of the counter to 10 
            else:             #then other functions using counter will also have counter value as 10.
                display=str(counter) #the counter_label is accepting the argument label.

            lbl['text']=display    
                               #Global counter, here we are calling the variable counter which is outside this function.
                               #Till the time counter is -1 it will display 00 on the screen.
            lbl.after(1000, count)  #The moment user will click on the action button this function will be activated and the counter will keep on increasing from -1 to n.
                                    
            counter += 1           #this function will return the current counter time
    count()                         #count() is another function passed in counter_label.

def StartTimer(lbl):
    global running                #Global counter, here we are calling the variable counter which is outside this function.
    running=True                    # means if running == True will work until set to false 
    counter_label(lbl)              #is another function passed in counter_label.
    start_btn['state']='disabled' 
    stop_btn['state']='normal'
    reset_btn['state']='normal'

def StopTimer():            # will function will be called when when user clicks the stop button
    global running                #function will stop now.
    start_btn['state']='normal'   
    stop_btn['state']='disabled'  #it will disable the stop button & the user won’t beable to click 
    reset_btn['state']='normal'  #will enable the start & reset buttons
    running = False
#The reset function is called when the user clicks on the Reset button.
def ResetTimer(lbl):    #user either can resume the counter by clicking on the start button or can reset it
    global counter            #Global counter, here we are calling the variable counter which is outside this function.
    counter=-1         #The counter will again et to default value i.e -1
    if running==False:      #Running will set to false and text appearing on the main application window will be set to 00.
        reset_btn['state']='disabled'
        lbl['text']='00' #label_msg
    else:                          
        lbl['text']=''  #label_msg

#bg = PhotoImage(file='stopwatch.png')
#img = Label(ws, image=bg, bg='#299617')
#img.place(x=75, y=50)
#Labels 
lbl = Label(ws,text="00",fg="black", bg='#299617',font="Verdana 40 bold")

label_msg = Label(ws, text="seconds",fg="black",bg='#299617',font="Verdana 10 bold")

lbl.place(x=160, y=170)
label_msg.place(x=170, y=250)

#Button Functions
start_btn=Button( ws, text='Start', width=15, command=lambda:StartTimer(lbl))
start_btn.place(x=30, y=390)

stop_btn = Button(ws,text='Stop',width=15,state='disabled',command=StopTimer)
stop_btn.place(x=150, y=390)

reset_btn = Button(ws, text='Reset',  width=15, state='disabled',command=lambda:ResetTimer(lbl))
reset_btn.place(x=270, y=390)


ws.mainloop()