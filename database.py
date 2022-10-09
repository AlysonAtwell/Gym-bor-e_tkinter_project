from tkinter import *

import sqlite3


root=Tk()
root.title("user_registration")

#Connect a database
conn = sqlite3.connect("user_registration.db")

#create curser
c = conn.cursor()

def submit():
    #Clear the Text boxes
    F_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, End)
    zipcode.delete(0, End)
    
    
    
# Creat Table
c.execute("""CREATE TABLE users(
    first_name text,
    last_name text,
    city text,
    state text,
    zipcode integer
    )""")

#Create Query function
def query():
    #Connect a database
    conn = sqlite3.connect('user_registration.db')
    #create curser
    c = conn.cursor()

    #Query the database
    c.execute("SELECT *, oid FROM addresses") 
    records + c.fetchall()
    print(records)
    
    #Loop Thur Results
    print_records =''
    for record in records[0]:
        print_records += str(record) + "\n"
        
    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)
    
#creat text boexes
f_name = Entry(root, width =30)
f_name.grid(row=0,column=1, padx=20)
l_name = Entry(root, width =30)
l_name.grid(row=1,column=1, padx=20)
address = Entry(root, width =30)
address.grid(row=2,column=1, padx=20)
city = Entry(root, width =30)
city.grid(row=3,column=1, padx=20)
state = Entry(root, width =30)
state.grid(row=4,column=1, padx=20)
zipcode = Entry(root, width =30)
zipcode.grid(row=5,column=1, padx=20)

#Create labels for text boxes
f_name_label = Label(root, text= "First Name")
f_name_label.grid(row=0,column=1, padx=20)
l_name_label = Label(root, text= "First Name")
l_name_label.grid(row=0,column=1, padx=20)
address_label = Label(root, text= "First Name")
address_label.grid(row=0,column=1, padx=20)
city_label = Label(root, text= "First Name")
city_label.grid(row=0,column=1, padx=20)
state_label = Label(root, text= "First Name")
state_label.grid(row=0,column=1, padx=20)
zipcode_label = Label(root, text= "First Name")
zipcode_label.grid(row=0,column=1, padx=20)

#Create Submit Button
submit_btn = Button(root, text="Submit", command=submit)
submit_btn.grid(row=0,column=1, columnspan=2, padx=10,pady=10,ipadx=100)


#committ changes
conn.commit()
#Close Connection
conn.close()
root.mainloop()