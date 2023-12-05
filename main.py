import PIL.Image
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.colorchooser import askcolor


root = Tk()
root.title("SketchBee")
root.geometry("750x550+100+100")
root.resizable(False,False)

# Icon 
image_icon = PhotoImage(file="bee2.png")
root.iconphoto(False,image_icon)

# Canvas for colors
colors = Canvas(root,width=37,height=310,bg="#ffffff",bd=0)
colors.place(x=20,y=40)

# Function for displaying the pallete 
def display_pallete():
    id = colors.create_rectangle((10,10,30,30),fill='black')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('black'))

    id = colors.create_rectangle((10,40,30,60),fill='red')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('red'))

    id = colors.create_rectangle((10,70,30,90),fill='green')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('green'))

    id = colors.create_rectangle((10,100,30,120),fill='blue')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('blue'))

    id = colors.create_rectangle((10,130,30,150),fill='yellow')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('yellow'))

    id = colors.create_rectangle((10,160,30,180),fill='orange')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('orange'))

    id = colors.create_rectangle((10,190,30,210),fill='brown4')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('brown4'))

    id = colors.create_rectangle((10,220,30,240),fill='gray')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('gray'))

    id = colors.create_rectangle((10,250,30,270),fill='lightblue')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('lightblue'))

    id = colors.create_rectangle((10,280,30,300),fill='purple')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('purple'))

display_pallete()

currX=0
currY=0
color = 'black'

# Function for finding x and y coor.
def locate_xy(work):
    global currX,currY
    currX = work.x
    currY = work.y

# Function for drawing
def addLine(work):
    global currX,currY
    canvas.create_line((currX,currY,work.x,work.y),width=getSliderVal(),fill=color,capstyle=ROUND,smooth=True)
    currX,currY = work.x,work.y

# Function for picking color from the pallete

def show_color(new_Col):
    global color
    color = new_Col

# Eraser command function

def newCanvas():
    canvas.delete('all')
    display_pallete()
    
# Eraser
im = PIL.Image.open("eraser.png")
resizedEraser = im.resize((25,25))
resizedEraser.save("new_eraser.png","PNG")
eraser = PhotoImage(file='new_eraser.png')
Button(root,image=eraser,command=newCanvas,bg="gray").place(x=25,y=370)

# Canvas for drawing
canvas = Canvas(root,width=600,cursor="hand2",height=450,background="white")
canvas.place(x=100,y=10)

canvas.bind('<Button-1>',locate_xy)
canvas.bind('<B1-Motion>',addLine)


#Slider

# Function upon changing the slider
def slider_changed(e):
    slider_val.configure(text=getSliderVal())

# var to keep track of slider value
curr_val=DoubleVar()
slider = ttk.Scale(root,from_=0,to=100,orient='horizontal',command=slider_changed,variable=curr_val)
slider.place(x=10,y=500)

# Function to get the value of the slider
def getSliderVal():
    return '{: .2f}'.format(curr_val.get())

slider_val = ttk.Label(root,text=getSliderVal())
slider_val.place(x=120,y=500)
root.mainloop()