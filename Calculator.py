#Calculator.py

#Create a calculator, create the divide button, multiply,addition, subtraction, equals.
#Create the numbers for the calculators as well
#Make sure the buttons work
from tkinter import*
screen=Tk()
screen.geometry("450x500")
def one():
    
    E1.insert(END,1)
def two():
    E1.insert(END,2)
def three():
    E1.insert(END,3)
def four():
    E1.insert(END,4)
def five():
    E1.insert(END,5)
def six():
    E1.insert(END,6)
def seven():
    E1.insert(END,7)
def eight():
    E1.insert(END,8)
def nine():
    E1.insert(END,9)
def zero():
    E1.insert(END,0)
def CE():
    E1.delete(0,END)
def plus():
    global number1
    number1=E1.get()
    number1=float(number1)
    
    E1.delete(0,END)
    global sign
    sign=1
def equal():
    number2=E1.get()
    number2=float(number2)
    E1.delete(0,END)
    if sign==1:
        answer=number1+number2
    if sign==2:
        answer=number1-number2
    if sign==3:
        answer=number1*number2
    if sign==4:
        answer=number1/number2
    if sign==5:
        answer=number1*number2/100    
    E1.insert(END,answer)
def minus():
    global number1
    number1=E1.get()
    number1=float(number1)
    E1.delete(0,END)
    global sign
    sign=2
def multiply():
    global number1
    number1=E1.get()
    number1=float(number1)
    E1.delete(0,END)
    global sign
    sign=3
def divide():
    global number1
    number1=E1.get()
    number1=float(number1)
    E1.delete(0,END)
    global sign
    sign=4
def percentage():
    global number1
    number1=E1.get()
    number1=float(number1)
    E1.delete(0,END)
    global sign
    sign=5
def dot():
    E1.insert(END,'.')
L1=Label(screen,text="Calculator")
def backspace():
    E1.delete(0,1)
def squared():
    global number1
    number1=E1.get()
    number1=float(number1)
    number1=number1*number1
    E1.delete(0,END)
    E1.insert(END,number1)
L1.grid(row=0,column=0)
E1=Entry(screen,width=50)
E1.grid(row=1,column=1)
B1=Button(screen,text=" 1 ",height=3,width=5,command=one)
B1.grid(row=2,column=0)
B2=Button(screen,text=" 2 ",height=3,width=5,command=two)
B2.grid(row=2,column=1)
B3=Button(screen,text=" 3 ",height=3,width=5,command=three)
B3.grid(row=2,column=2)
B4=Button(screen,text=" 4 ",height=3,width=5,command=four)
B4.grid(row=3,column=0)
B5=Button(screen,text=" 5 ",height=3,width=5,command=five)
B5.grid(row=3,column=1)
B6=Button(screen,text=" 6 ",height=3,width=5,command=six)
B6.grid(row=3,column=2)
B7=Button(screen,text=" 7 ",height=3,width=5,command=seven)
B7.grid(row=4,column=0)
B8=Button(screen,text=" 8 ",height=3,width=5,command=eight)
B8.grid(row=4,column=1)
B9=Button(screen,text=" 9 ",height=3,width=5,command=nine)
B9.grid(row=4,column=2)
B10=Button(screen,text=" 0 ",height=3,width=5,command=zero)
B10.grid(row=5,column=1)
B11=Button(screen,text=" . ",height=3,width=5,command=dot)
B11.grid(row=5,column=2)
B12=Button(screen,text=" CE ",height=3,width=5,command=CE)
B12.grid(row=5,column=0)
B13=Button(screen,text=" + ",height=3,width=5,command=plus)
B13.grid(row=6,column=0)
B14=Button(screen,text=" - ",height=3,width=5,command=minus)
B14.grid(row=6,column=1)
B15=Button(screen,text=" / ",height=3,width=5,command=divide)
B15.grid(row=6,column=2)
B16=Button(screen,text=" % ",height=3,width=5,command=percentage)
B16.grid(row=7,column=1)
B17=Button(screen,text=" = ",height=3,width=5,command=equal)
B17.grid(row=7,column=2)
B18=Button(screen,text=" X ",height=3,width=5,command=multiply)
B18.grid(row=7,column=0)
B19=Button(screen,text="<--",height=3,width=5,command=backspace)
B19.grid(row=8,column=0)
B20=Button(screen,text="(",height=3,width=5)
B20.grid(row=8,column=1)
B21=Button(screen,text=")",height=3,width=5)
B21.grid(row=8,column=2)
B22=Button(screen,text="X**2",height=3,width=5,command=squared)
B22.grid(row=9,column=0)
B23=Button(screen,text="\/",height=3,width=5)
B23.grid(row=9,column=1)
B24=Button(screen,text="1/X",height=3,width=5)
B24.grid(row=9,column=2)
