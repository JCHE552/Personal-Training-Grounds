from tkinter import*
from buttons import buttons
from top import*

root =Tk()#creates window

top.top_box(root)#creates the top box or entry in calc app


for i in range(10):#creates buttons for numbers 0 to 9
	btn = buttons(i)
	btn.create_btn_object(root)#creates them on the window
	btn.buttons_btn_object.grid(row = (i+3)//3, column = (i+3)%3)#positions buttons

operation = ['+','-','x','/','=','CE','Clear','(',')' ]#array that contains operators

for j in range(len(operation)):#creates buttons for operators
	btn1 = buttons(operation[j])
	btn1.create_btn_object(root)#creates them on window
	btn1.buttons_btn_object.grid(row = (13+j)//3, column = (13+j)%3)#positions buttons





root.mainloop()