import tkinter as tk
import random

gm=tk.Tk()
# gm.geometry("400x400")
gm.configure(bg="#000000")
gm.title("RSP game")
gm.iconbitmap("hnet.com-image.ico")

u_score=0
c_score=0

u_choice=""
c_choice=""
def com_choice_random():
    return random.choice(["rock","paper","scissor"])
# print(com_choice_random())

def choice_to_num(choice):
        rps = {'rock': 0, 'paper': 1, 'scissor': 2}
        return rps[choice]

def num_to_choice(number):
    rps = {0: 'rock', 1: 'paper', 2: 'scissor'}
    return rps[number]

def result(u_choice,c_choice):
    global c_score
    global u_score
    user=choice_to_num(u_choice)
    comp=choice_to_num(c_choice)
    if (user==comp):
        print("equal")
    elif((user-comp)%3==1):
        print("congratulation ,You win")
        u_score+=1
    else:
        print("computer wins")
        c_score+=1
    area=tk.Text(master=gm,height=14,width=35,bg="#ffffcc")
    area.grid(column=0,row=4)
    res="Your choice is :{uc} \nComputer's choice: {cc}\nyour Score is : {us}\ncomputer Score : {cs} ".format(uc=u_choice,cc=c_choice,us=u_score,cs=c_score)
    area.insert(tk.END,res)

def rock():
    global u_choice
    global c_choice
    u_choice='rock'
    c_choice=com_choice_random()
    result(u_choice,c_choice)

photo_rock = tk.PhotoImage(file = "stone.png")
but_rock=tk.Button(text="            Rock",bg="#ffff00",command=rock,image=photo_rock)
but_rock.grid(column=0,row=1)

def paper():
    global u_choice
    global c_choice
    u_choice='paper'
    c_choice=com_choice_random()
    result(u_choice,c_choice)

photo_paper = tk.PhotoImage(file = "idea.png")
but_paper=tk.Button(text="            Paper  ",bg="#ff3399",command=paper,image=photo_paper)
but_paper.grid(column=0,row=2)


def scissor():
    global u_choice
    global c_choice
    u_choice='scissor'
    c_choice=com_choice_random()
    result(u_choice,c_choice)

photo_sc = tk.PhotoImage(file = "scissors.png")
but_sc=tk.Button(text="            Scissors ",bg="#6699ff",command=scissor,image=photo_sc)
but_sc.grid(column=0,row=3)


gm.mainloop()