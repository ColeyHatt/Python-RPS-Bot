import random
import tkinter as tk

attempt = 0
win = 0
lose = 0
#1 = Paper
#2 = Rock
#3 = Scissors
def rock():
    global attempt
    attempt = attempt + 1
    rps = random.randint(1, 3)  #computers choice
    if rps == 1:
        RvPLabel = tk.Label(text="You lose, try again.")
        RvPLabel.pack()
    if rps == 2:
        RvRLabel = tk.Label(text="Draw, try again.")
        RvRLabel.pack()
    if rps == 3:
        RvSLabel = tk.Label(text="You win! Try again?")
        RvSLabel.pack()
        
def paper():
    global attempt
    attempt = attempt + 1
    rps = random.randint(1, 3)  #computers choice
    if rps == 1:
        SvPLabel = tk.Label(text="You lose, try again.")
        SvPLabel.pack()
    if rps == 2:
        PvPLabel = tk.Label(text="Draw, try again.")
        PvPLabel.pack()
    if rps == 3:
        PvRLabel = tk.Label(text="You win! Try again?")
        PvRLabel.pack()
        
def scissors():
    global attempt
    attempt = attempt + 1
    rps = random.randint(1, 3)  #computers choice
    if rps == 1:
        SvPLabel = tk.Label(text="You lose, try again.")
        SvPLabel.pack()
    if rps == 2:
        SvSLabel = tk.Label(text="Draw, try again.")
        SvSLabel.pack()
    if rps == 3:
        SvRLabel = tk.Label(text="You win! Try again?")
        SvRLabel.pack()

window = tk.Tk()

window.title("Rock Paper Scissors")
greeting = tk.Label(text="Rock Paper Scissors?")
greeting.pack()

Rbutton = tk.Button(text="Rock", command = rock)
Rbutton.pack(side=tk.TOP)
Pbutton = tk.Button(text="Paper", command = paper)
Pbutton.pack(side=tk.TOP)
Sbutton = tk.Button(text="Scissors", command = scissors)
Sbutton.pack(side=tk.TOP)
window.mainloop()

