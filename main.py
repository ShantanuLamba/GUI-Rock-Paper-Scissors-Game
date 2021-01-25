from tkinter import *
import random
root = Tk()
def rockcmd():
    compchoice = random.randint(1, 3)
    if compchoice == 3:
        labeltellx = Label(text="Computer has chosen Scissors")
        labeltellx.pack()
        labelx = Label(text="You Win")
        labelx.pack()
    elif compchoice == 1:
        labeltellx = Label(text="Computer has chosen Rock")
        labeltellx.pack()
        labelx = Label(text="Tie")
        labelx.pack()
    else:
        labeltellx = Label(text="Computer has chosen Paper")
        labeltellx.pack()
        labelx = Label(text="You loose")
        labelx.pack()
def papercmd():
    compchoice = random.randint(1, 3)
    if compchoice == 1:
        labeltellx = Label(text="Computer has chosen Rock")
        labeltellx.pack()
        labelx = Label(text="You Win")
        labelx.pack()
    elif compchoice == 2:
        labeltellx = Label(text="Computer has chosen Paper")
        labeltellx.pack()
        labelx = Label(text="Tie")
        labelx.pack()
    else:
        labeltellx = Label(text="Computer has chosen Scissors")
        labeltellx.pack()
        labelx = Label(text="You loose")
        labelx.pack()
def scissorscmd():
    compchoice = random.randint(1, 3)
    if compchoice == 2:
        labeltellx = Label(text="Computer has chosen Paper")
        labeltellx.pack()
        labelx = Label(text="You Win")
        labelx.pack()
    elif compchoice == 3:
        labeltellx = Label(text="Computer has chosen Scissors")
        labeltellx.pack()
        labelx = Label(text="Tie")
        labelx.pack()
    else:
        labeltellx = Label(text="Computer has chosen Rock")
        labeltellx.pack()
        labelx = Label(text="You loose")
        labelx.pack()

root.minsize(650, 780)
root.maxsize(650, 780)
root.title("Rock, Paper, Scissors Game")

Title = Label(text="Rock, Paper, Scissors Game", bg="red", fg="white", font="fan 19 bold", borderwidth= 3,relief=GROOVE)
Title.pack(fill=X)

Label1 = Label(text="Choose between Rock, Paper and Scissors", font="hehe 13 ")
Label1.pack(pady=5)

photo = PhotoImage(file="title-image (1).png")
photolabel = Label(image=photo)
photolabel.pack()

rockphoto = PhotoImage(file="rock_100x100.png")
rockphotolabel = Label(image=rockphoto)
rockphotolabel.pack(pady=3)
rockbtn = Button(text="ROCK",font="helvetica 14 bold", bg="yellow", fg="orange", command=rockcmd).pack()
paperphoto = PhotoImage(file="paper_100x100.png")
paperphotolabel = Label(image=paperphoto)
paperphotolabel.pack(pady=3)
paperbtn = Button(text="PAPER",font="helvetica 14 bold", bg="yellow", fg="orange", command=papercmd).pack()
scissorphoto = PhotoImage(file="scissor_100x100.png")
scissorphotolabel = Label(image=scissorphoto)
scissorphotolabel.pack(pady=3)
scissorbtn = Button(text="SCISSORS",font="helvetica 14 bold", bg="yellow", fg="orange", command=scissorscmd).pack()


root.mainloop()
