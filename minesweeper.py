from tkinter import*
from cell import cell
import start
import settings
from cell2 import cell2


root1 = Tk()

root1.geometry(f'{start.WIDTH}x{start.HEIGHT}')#1440x720
root1.title("minesweeper")#creates title
root1.resizable(False,False)#makes sure you can't change dimensions of the window
root1.configure(bg="white")#makes the background black



top_frame1 = Frame(#create top frame
	root1, bg="white", width = start.WIDTH, height = settings.height_prct(25)
	)
top_frame1.place(x=0,y=0)#positions top frame

left_frame1 = Frame(#creates left frame
	root1, bg = "white", width = settings.width_prct(25), height = settings.height_prct(100)
	)
left_frame1.place(x=0, y=180)#positions left frame




center_frame1 = Frame(#creates center frame
	root1, bg = "white", width = settings.width_prct(75), height = settings.height_prct(75)
	)
center_frame1.place(x=settings.width_prct(25), y=settings.height_prct(25))#positions center frame


cell2.create_label(top_frame1)
cell2.create_label.place(x=45, y=10)


#creates grid for minesweeper
for i in range(start.rownum):#proceed by rows
	for j in range(start.colnum):#proceed by cols
		c3 = cell2(i, j)#creates object with indices i and j
		c3.create_btn_object1(center_frame1)#creates object in center frame
		c3.cell_btn_object1.grid(#positions the object
			column=j, row=i
		)




root1.mainloop() #runs the window





#configure settings of window
root = Tk()
root.geometry(f'{start.WIDTH}x{start.HEIGHT}')#1440x720
root.title("minesweeper")#creates title
root.resizable(False,False)#makes sure you can't change dimensions of the window
root.configure(bg="white")#makes the background white
top_frame = Frame(#create top frame
	root, bg="white", width = start.WIDTH, height = settings.height_prct(25)
	)
top_frame.place(x=0,y=0)#positions top frame

left_frame = Frame(#creates left frame
	root, bg = "white", width = settings.width_prct(25), height = settings.height_prct(100)
	)
left_frame.place(x=0, y=180)#positions left frame

center_frame = Frame(#creates center frame
	root, bg = "white", width = settings.width_prct(75), height = settings.height_prct(75)
	)
center_frame.place(x=settings.width_prct(25), y=settings.height_prct(25))#positions center frame




#creates grid for minesweeper
for i in range(start.rownum1):#proceed by rows
	for j in range(start.colnum1):#proceed by cols
		c3 = cell(i, j)#creates object with indices i and jif start.cellcount == 0:
		c3.create_btn_object(center_frame)#creates object in center frame
		c3.cell_btn_object.grid(#positions the object
			column=j, row=i
		)

print(len(cell.all))#prints number of cells
cell.randomize_mines()

for c in cell.all:
	print(c.is_mine)

cell.create_label2(top_frame)
cell.create_label2.place(x=45, y=10)

cell.create_label3(left_frame)
cell.create_label3.place(x=45, y=10)



root.mainloop()