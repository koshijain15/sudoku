import random
from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Sudoku")

#p1 = PhotoImage(file = 'sudoku.png')
#root.iconphoto(False, p1)

n=random.randint(0,1)
puzz=[[(0,7,9,8,0,2,0,6,3),(6,0,0,9,0,0,0,1,0),(8,0,3,0,7,0,0,0,2),(0,9,0,0,0,0,3,7,1),(0,6,8,7,0,0,0,9,0),(0,3,1,0,2,0,5,8,0),(2,8,6,5,0,0,1,3,0),(0,0,0,0,0,0,0,0,0),(9,0,4,3,0,0,8,2,7)],[(5,3,0,0,7,0,0,0,0),(6,0,0,1,9,5,0,0,0),(0,9,8,0,0,0,0,6,0),(8,0,0,0,6,0,0,0,3),(4,0,0,8,0,3,0,0,1),(7,0,0,0,2,0,0,0,6),(0,6,0,0,0,0,2,8,0),(0,0,0,4,1,9,0,0,5),(0,0,0,0,8,0,0,7,9)]]
sol=[[(1,7,9,8,5,2,4,6,3),(6,2,5,9,3,4,7,1,8),(8,4,3,1,7,6,9,5,2),(4,9,2,6,8,5,3,7,1),(5,6,8,7,1,3,2,9,4),(7,3,1,4,2,9,5,8,6),(2,8,6,5,4,7,1,3,9),(3,1,7,2,9,8,6,4,5),(9,5,4,3,6,1,8,2,7)],[(5,3,4,6,7,8,9,1,2),(6,7,2,1,9,5,3,4,8),(1,9,8,3,4,2,5,6,7),(8,5,9,7,6,1,4,2,3),(4,2,6,8,5,3,7,9,1),(7,1,3,9,2,4,8,5,6),(9,6,1,5,3,7,2,8,4),(2,8,7,4,1,9,6,3,5),(3,4,5,2,8,6,1,7,9)]]
arr=puzz[n]
arr1=sol[n]
n1=(n+1)%2

def help_fun():
     top=Tk()
     top.title("Rules")
     top.geometry("400x150")
     Label(top,text="Sudoku Rules\n").pack()
     Label(top,text="1) A 9x9 square must be filled with numbers from 1-9 with",anchor="w",justify="left",width=250).pack()
     Label(top,text="no repeated numbers in each lines,horizontally or vertically.\n",anchor="w",justify="left",width=250).pack()
     Label(top,text="2) To challenge you more there are 3x3 squares marked out in",anchor="w",justify="left",width=250).pack()
     Label(top,text="a grid and each of these squares can't have any repeat numbers.",anchor="w",justify="left",width=250).pack()

def instructions():
    top=Tk()
    top.title("Instructions")
    top.geometry("300x100")
    Label(top,text="Clear: It will delete all the entries inserted.",anchor="w",justify="left",width=250).pack()
    Label(top,text="Check: Click check to see if all the entries are right.",anchor="w",justify="left",width=250).pack()
    Label(top,text="Hint : Click hint to get a a randomly generated entry.",anchor="w",justify="left",width=250).pack()

def clear_fun():
    for i in entry:
        i.delete(0,END)

def check_fun():
    f=1
    k=0
    
    for i in range(3):
        for j in range(3):
            if(arr[i][j]==0):
                num=entry[k].get()
                if(num=="" or int(num)!=arr1[i][j]):
                    f=0
                    break
                k=k+1
    if(f!=0):
        for i in range(3):
            for j in range(3):
                if(arr[i][j+3]==0):
                    num=entry[k].get()
                    if(num=="" or int(num)!=arr1[i][j+3]):
                        f=0
                        break
                    k=k+1
    if(f!=0):
        for i in range(3):
            for j in range(3):
                if(arr[i][j+6]==0):
                    num=entry[k].get()
                    if(num=="" or int(num)!=arr1[i][j+6]):
                        f=0
                        break
                    k=k+1
    if(f!=0):
        for i in range(3):
            for j in range(3):
                if(arr[i+3][j]==0):
                    num=entry[k].get()
                    if(num=="" or int(num)!=arr1[i+3][j]):
                        f=0
                        break
                    k=k+1
    if(f!=0):
        for i in range(3):
            for j in range(3):
                if(arr[i+3][j+3]==0):
                    num=entry[k].get()
                    if(num=="" or int(num)!=arr1[i+3][j+3]):
                        f=0
                        break
                    k=k+1
    if(f!=0):
        for i in range(3):
            for j in range(3):
                if(arr[i+3][j+6]==0):
                    num=entry[k].get()
                    if(num=="" or int(num)!=arr1[i+3][j+6]):
                        f=0
                        break
                    k=k+1
    if(f!=0):
        for i in range(3):
            for j in range(3):
                if(arr[i+6][j]==0):
                    num=entry[k].get()
                    if(num=="" or int(num)!=arr1[i+6][j]):
                        f=0
                        break
                    k=k+1
    if(f!=0):
        for i in range(3):
            for j in range(3):
                if(arr[i+6][j+3]==0):
                    num=entry[k].get()
                    if(num=="" or int(num)!=arr1[i+6][j+3]):
                        f=0
                        break
                    k=k+1
    if(f!=0):
        for i in range(3):
            for j in range(3):
                if(arr[i+6][j+6]==0):
                    num=entry[k].get()
                    if(num=="" or int(num)!=arr1[i+6][j+6]):
                        f=0
                        break
                    k=k+1
    new=Tk()
    new.geometry("400x100")
    new.title("Result")
    if(f==0):
        Label(new,text="").pack()
        Label(new,text="").pack()
        Label(new,text="Something is wrong.Check again.",font=("Arial",10)).pack()
    else:
        Label(new,text="").pack()
        Label(new,text="").pack()
        Label(new,text="You won!!",font=("Arial",10)).pack()

def hint_fun():
    f=0
    i=random.randint(0,len(value)-1)
    n=i
    while(i<len(value) and entry[i].get()!=""):
        i=i+1
    if(i==len(value)):
        i=0
        while(i<n and entry[i].get()!=""):
            i=i+1
    if(entry[i].get()==""):
        entry[i].insert(0,value[i])

def solution_fun():
    for i in range(0,len(value)):
        if(entry[i].get()==""):
            entry[i].insert(0,value[i])




title=Label(root,text="SUDOKU",font=("Arial",20,"bold"))
title.grid(row=0,column=0,columnspan=3)


entry=[]
value=[]

option=Menu(root)
help_option=Menu(option)
option.add_cascade(label="Help",menu=help_option)
help_option.add_command(label="Rules",command=help_fun)
help_option.add_command(label="Instructions",command=instructions)
options_option=Menu(option)
option.add_cascade(label="Options",menu=options_option)
options_option.add_command(label="Check",command=check_fun)
options_option.add_command(label="Clear",command=clear_fun)
options_option.add_command(label="Hint",command=hint_fun)
options_option.add_command(label="Solution",command=solution_fun)


def display():
    panel1=PanedWindow(bd=4,relief="raised")
    panel1.grid(row=1,column=0)
    for i in range (3):
        for j in range(3):
            if(arr[i][j]==0):
                entrybox=Entry(panel1,bd=1,width=4,justify="center",font=("Arial",10))
                entry.append(entrybox)
                value.append(arr1[i][j])
                panel1.add(entrybox)
                entrybox.grid(row=i,column=j)
            else:
                border=Frame
                label=Label(panel1,bd=1,text=arr[i][j],width=3,font=("Arial",10))
                
                panel1.add(label)
                label.grid(row=i,column=j)
    panel2=PanedWindow(bd=4,relief="raised")
    panel2.grid(row=1,column=1)
    for i in range (3):
        for j in range(3):
            if(arr[i][j+3]==0):
                entrybox=Entry(panel2,bd=1,width=4,font=("Arial",10),justify="center")
                entry.append(entrybox)
                value.append(arr1[i][j+3])
                panel2.add(entrybox)
                entrybox.grid(row=i,column=j)
            else:
                label=Label(panel2,bd=1,text=arr[i][j+3],width=3,font=("Arial",10))
                panel2.add(label)
                label.grid(row=i,column=j)
    panel3=PanedWindow(bd=4,relief="raised")
    panel3.grid(row=1,column=2)
    for i in range (3):
        for j in range(3):
            if(arr[i][j+6]==0):
                entrybox=Entry(panel3,bd=1,width=4,font=("Arial",10),justify="center")
                entry.append(entrybox)
                value.append(arr1[i][j+6])
                panel3.add(entrybox)
                entrybox.grid(row=i,column=j)
            else:
                label=Label(panel3,bd=1,text=arr[i][j+6],width=3,font=("Arial",10))
                panel3.add(label)
                label.grid(row=i,column=j)
    panel4=PanedWindow(bd=4,relief="raised")
    panel4.grid(row=2,column=0)
    for i in range (3):
        for j in range(3):
            if(arr[i+3][j]==0):
                entrybox=Entry(panel4,bd=1,width=4,font=("Arial",10),justify="center")
                entry.append(entrybox)
                value.append(arr1[i+3][j])
                panel4.add(entrybox)
                entrybox.grid(row=i,column=j)
            else:
                label=Label(panel4,bd=1,text=arr[i+3][j],width=3,font=("Arial",10))
                panel4.add(label)
                label.grid(row=i,column=j)
    panel5=PanedWindow(bd=4,relief="raised")
    panel5.grid(row=2,column=1)
    for i in range (3):
        for j in range(3):
            if(arr[i+3][j+3]==0):
                entrybox=Entry(panel5,bd=1,width=4,font=("Arial",10),justify="center")
                entry.append(entrybox)
                value.append(arr1[i+3][j+3])
                panel5.add(entrybox)
                entrybox.grid(row=i,column=j)
            else:
                label=Label(panel5,bd=1,text=arr[i+3][j+3],width=3,font=("Arial",10))
                panel5.add(label)
                label.grid(row=i,column=j)
    panel6=PanedWindow(bd=4,relief="raised")
    panel6.grid(row=2,column=2)
    for i in range (3):
        for j in range(3):
            if(arr[i+3][j+6]==0):
                entrybox=Entry(panel6,bd=1,width=4,font=("Arial",10),justify="center")
                entry.append(entrybox)
                value.append(arr1[i+3][j+6])
                panel6.add(entrybox)
                entrybox.grid(row=i,column=j)
            else:
                label=Label(panel6,bd=1,text=arr[i+3][j+6],width=3,font=("Arial",10))
                panel6.add(label)
                label.grid(row=i,column=j)
    panel7=PanedWindow(bd=4,relief="raised")
    panel7.grid(row=3,column=0)
    for i in range (3):
        for j in range(3):
            if(arr[i+6][j]==0):
                entrybox=Entry(panel7,bd=1,width=4,font=("Arial",10),justify="center")
                entry.append(entrybox)
                value.append(arr1[i+6][j])
                panel7.add(entrybox)
                entrybox.grid(row=i,column=j)
            else:
                label=Label(panel7,bd=1,text=arr[i+6][j],width=3,font=("Arial",10))
                panel7.add(label)
                label.grid(row=i,column=j)
    panel8=PanedWindow(bd=4,relief="raised")
    panel8.grid(row=3,column=1)
    for i in range (3):
        for j in range(3):
            if(arr[i+6][j+3]==0):
                entrybox=Entry(panel8,bd=1,width=4,font=("Arial",10),justify="center")
                entry.append(entrybox)
                value.append(arr1[i+6][j+3])
                panel8.add(entrybox)
                entrybox.grid(row=i,column=j)
            else:
                label=Label(panel8,bd=1,text=arr[i+6][j+3],width=3,font=("Arial",10))
                panel8.add(label)
                label.grid(row=i,column=j)
    panel9=PanedWindow(bd=4,relief="raised")
    panel9.grid(row=3,column=2)
    for i in range (3):
        for j in range(3):
            if(arr[i+6][j+6]==0):
                entrybox=Entry(panel9,bd=1,width=4,font=("Arial",10),justify="center")
                entry.append(entrybox)
                value.append(arr1[i+6][j+6])
                panel9.add(entrybox)
                entrybox.grid(row=i,column=j)
            else:
                label=Label(panel9,bd=1,text=arr[i+6][j+6],width=3,font=("Arial",10))
                panel9.add(label)
                label.grid(row=i,column=j)

display()
Label(root,text="").grid(row=4,column=0)
clear=Button(root,text="Clear",width=43,command=clear_fun)
clear.grid(row=5,column=0,columnspan=3)
check=Button(root,text="Check",width=43,command=check_fun)
check.grid(row=6,column=0,columnspan=3)
hint=Button(root,text="Hint",width=43,command=hint_fun)
hint.grid(row=7,column=0,columnspan=3)
root.config(menu=option)
mainloop()