from tkinter import *#importing tkinter library of python
import random #importing random function so as to use it later on in randint

def raise_frame(frame):
	frame.tkraise()


root = Tk()#to create separate window(it is like a container)
root.title("Guess the number !!")
root.geometry('550x400')
root.configure(background="LightCyan2")

title=Label(root,text="Guess the number!",font=("times new roman",18,"bold"),bg="LightCyan2")
title.pack(side=TOP,fill=X)

f1 = Frame(root, borderwidth=4, bg="thistle", relief=GROOVE)
f2 = Frame(root, borderwidth=4, bg="thistle", relief=GROOVE)
f3 = Frame(root, borderwidth=4, bg="thistle", relief=GROOVE)

for frame in (f1,f2, f3):
	frame.place(x=25,y=35,width=500,height=350)

raise_frame(f1)


comment_1 = Label(f1, text="Get ready friends😉\n Let us play a intersting game\nGetting excited🤩🤩!",font=("times new roman",16,"bold"), bg="thistle")
comment_1.pack(anchor="n",padx=10,pady=5)

comment_2 = Label(f1, text="Please enter your names",font=("times new roman",12,"bold"), bg="thistle")#it is asking the player  to write names of players
comment_2.pack(anchor="nw",padx=10,pady=5)

name_1 = Label(f1, text="Player 1: ",font=("times new roman",12,"bold"), bg="thistle")
name_1.pack(anchor="nw",padx=10,pady=5)

#Entry key is to create a space to take input from user
e1 = Entry(f1, width=50)
e1.pack(anchor="nw",padx=10,pady=5)

name_2 = Label(f1, text="Player 2: ",font=("times new roman",12,"bold"), bg="thistle")
name_2.pack(anchor="nw",padx=10,pady=5)

e2 = Entry(f1, width=50)
e2.pack(anchor="nw",padx=10,pady=5)
p1=""
p2=""
def play():
    raise_frame(f2)
    global p1
    p1=e1.get()
    global p2
    p2=e2.get()
    global txt
    txt ="\nNow lets start the game!\n"+p1+"! Enter the Range.\n"
    comment_3 = Label(f2, text=txt,font=("times new roman",14,"bold"), bg="thistle")

    comment_3.pack(anchor="n",padx=10,pady=5)

    starting_guess = Label(f2, text="Starting guess: ",font=("times new roman",12,"bold"), bg="thistle")
    starting_guess.pack(anchor="w",padx=10,pady=5)

    global start
    start=StringVar()
    e3 = Entry(f2, width=50,textvariable=start)
    e3.pack(anchor="w",padx=10,pady=5)

    ending_guess = Label(f2, text="Ending guess: ",font=("times new roman",12,"bold"), bg="thistle")
    ending_guess.pack(anchor="w",padx=10,pady=5)

    global end
    end=StringVar()
    e4 = Entry(f2, width=50,textvariable=end)
    e4.pack(anchor="w",padx=10,pady=5)


    comment_4 = Label(f2, text=f"{p2} !! Let's start guessing in between given range by {p1}", bg="thistle")
    comment_4.pack(anchor="n",padx=10,pady=5)
    
    my_button = Button(f2, text="Start", command=button,font=("times new roman",12,"bold"))
    my_button.pack(anchor="n",padx=10,pady=10)
    
    

my_button = Button(f1, text="Let's Play", command=play,font=("times new roman",12,"bold"))
my_button.pack(anchor="s",padx=30,pady=10)


def random_number():
    global start_guess
    start_guess = int(start.get())
    global end_guess
    end_guess = int(end.get())
    return random.randint(start_guess, end_guess)

def optimal_ways():
    global start_guess
    global end_guess
    global guess_number
    optimal_ways = 0
    while ( start_guess <= end_guess):
        optimal_ways+=1
        k = (start_guess+end_guess)//2
        if ( k == guess_number) :
            break
        elif(k > guess_number):
            end_guess = (k-1)
        else:
            start_guess = (k + 1)
    
    return optimal_ways

def button():
    raise_frame(f3)

    global guess_number
    guess_number = random_number()

    global count_number
    count_number = 0

    global number_optimal_ways
    number_optimal_ways = optimal_ways()

    comment_4 = Label(f3, text="Enter your guess!!",font=("Times New Roman",12,"bold"), bg="thistle")
    comment_4.place(x=215,y=2)
        
    e = Entry(f3, width=38, borderwidth=5)
    e.place(x=40,y=30)

    #creating a function for button
    def button_click(number):
        current = e.get()
        global guess
        guess = int(str(current) + str(number))
        e.delete(0, END)
        e.insert(0, str(current) + str(number))

    #creating a function for exit button:
    def button_exit():
        root.destroy()

    #creating a function for deleting 
    def button_enter_function():
        global guess
        global count_number
        count_number = count_number + 1
        
        if guess == guess_number and count_number <= number_optimal_ways:
            l=[] 
            l.append(" Hurray!! you have won the game")
            l.append(" played well" )
            l.append(" Count: "+ str(count_number))

            button_exit_f3 = Button(f3, text="Exit",padx=30, pady=10, command=button_exit)
            button_exit_f3.place(x=330,y=210)

            e.delete(0, END)

        elif guess == guess_number and count_number > number_optimal_ways:
            l=[] 
            l.append(" You have lost the game")
            l.append(" better luck next time" )
            l.append(" Count: "+ str(count_number))

            button_exit_f3 = Button(f3, text="Exit",padx=30, pady=10, command=button_exit)
            button_exit_f3.place(x=330,y=210)

            e.delete(0, END)

        else:
            if guess < guess_number:
                l=[] 
                l.append(" Oops! wrong guess, try again.")
                l.append(" You should try greater than " + str(guess))
                l.append(" Count: "+ str(count_number))
  
                e.delete(0, END)
                
            else:
                l=[] 
                l.append(" Oops! wrong guess, try again.")
                l.append(" You should try lower than " + str(guess))
                l.append(" Count: "+ str(count_number))
                e.delete(0, END)

        listbox2.delete(0,END)
        for i in l:
            listbox2.insert(END,i)

    #creating buttons
    button_1 = Button(f3, text="1", padx=30, pady=15, command= lambda: button_click(1),font=("Times New Roman",12,"bold"))
    button_2 = Button(f3, text="2", padx=30, pady=15, command= lambda: button_click(2),font=("Times New Roman",12,"bold") )
    button_3 = Button(f3, text="3", padx=30, pady=15, command= lambda: button_click(3) ,font=("Times New Roman",12,"bold"))
    button_4 = Button(f3, text="4", padx=30, pady=15, command= lambda: button_click(4) ,font=("Times New Roman",12,"bold"))
    button_5 = Button(f3, text="5", padx=30, pady=15, command= lambda: button_click(5) ,font=("Times New Roman",12,"bold"))
    button_6 = Button(f3, text="6", padx=30, pady=15, command= lambda: button_click(6),font=("Times New Roman",12,"bold") )
    button_7 = Button(f3, text="7", padx=30, pady=15, command= lambda: button_click(7) ,font=("Times New Roman",12,"bold"))
    button_8 = Button(f3, text="8", padx=30, pady=15, command= lambda: button_click(8),font=("Times New Roman",12,"bold") )
    button_9 = Button(f3, text="9", padx=30, pady=15, command= lambda: button_click(9) ,font=("Times New Roman",12,"bold"))
    button_0 = Button(f3, text="0", padx=30, pady=15, command= lambda: button_click(0) ,font=("Times New Roman",12,"bold"))
    button_enter= Button(f3, text="Check", padx=24, pady=10, command= button_enter_function,font=("Times New Roman",12,"bold"))
    
    #put the button on screen
    button_1.place(x=35,y=70)
    button_2.place(x=125,y=70)
    button_3.place(x=215,y=70)
    button_4.place(x=35,y=140)
    button_5.place(x=125,y=140)
    button_6.place(x=215,y=140)
    button_7.place(x=35,y=210)
    button_8.place(x=125,y=210)
    button_9.place(x=215,y=210)
    button_0.place(x=125,y=280)
    button_enter.place(x=330,y=260)

    listbox2 = Listbox(f3,height=6,width=29)
    listbox2.place(x=300,y=100)

root.mainloop()


