
from tkinter import*
from top import*

class buttons:
	def __init__(self, oper, is_mine = False):#defines properties of buttons
		self.is_mine = is_mine
		self.buttons_btn_object = None
		self.oper = oper



	def create_btn_object(self, app):#creates object button with color, dimensions, and text
		btn = Button(
			app,
			width=4,
			height=2,
			bg="grey",
			text = self.oper,
		)

		btn.bind('<Button-1>',self.left_click_actions)#binds left click to a certain action

		self.buttons_btn_object = btn#binds properties to the object button

	

	def left_click_actions(self, event):#defines what left click action does

		if self.oper=='Clear':#if clear button was hit, it clears everything from top box
			top.top_box.delete(0, END)

			while len(top.allstack)>0:
				top.allstack.pop()

		elif self.oper=='CE':#if CE button was hit want to erase the most recent thing that was put (rightmost entry in topbox)
			top.top_box.delete(len(top.allstack)-1)
			top.allstack.pop()
				

		elif self.oper=='=':#will evaluate our expression if = button is clicked
			
			while len(top.allstack)>0 and top.d=='nonerror':#will pop off the allstack until empty
				
				c=top.allstack.pop(0)
				print(c)
				if isinstance(c,int):#checks if it is a digit and pops it
					
					
					top.numstack2.append(c)
					
					if len(top.allstack)>0:
						print('Hi')
						while len(top.allstack)>0 and isinstance(top.allstack[0],int):#will keep popping off digits until it hits operator
							
							top.numstack2.append(top.allstack.pop(0))
							print(top.numstack2)

					power = 0
					temp = 0
					while len(top.numstack2)>0:#will sum all the digits by base 10
						temp = temp + top.numstack2.pop()*(10**power)
						power = power + 1

					top.numstack.append(temp)#pushes the result onto numstack

				#handles operators
				elif c=='(':

					top.operstack.append('(')

				elif c==')':

					while not top.operstack[len(top.operstack)-1]=='(':

						output = buttons.opers(top.operstack.pop())
						top.numstack.append(output)

					top.operstack.append(c)

				elif c=='x' or c=='/' or c=='+' or c=='-':

					while len(top.operstack)>0 and (buttons.precedence(top.operstack[len(top.operstack)-1]) >= buttons.precedence(c)):
						print(buttons.precedence(top.operstack[len(top.operstack)-1]))
						print(buttons.precedence(c))
						output1 = buttons.opers(top.operstack.pop())
						
						top.numstack.append(output1)

					print(c)
					top.operstack.append(c)

				

			while len(top.operstack)>0 and len(top.numstack)>0 and top.d=='nonerror':
				print(top.numstack)
				print(top.operstack)
				output2 = buttons.opers(top.operstack.pop())
				if isinstance(output2,int):
					top.numstack.append(output2)

			while len(top.operstack)>0:
				top.operstack.pop()

			if top.d=='nonerror':
				final = top.numstack.pop()
				print(final)
				top.top_box.delete(0,END)
				top.top_box.insert(0,final)
				top.allstack.append(final)
			elif top.d=='error':
				top.top_box.delete(0,END)
				top.top_box.insert(0,'Can not divide by 0! Click Clear')
				top.d='nonerror'
				while len(top.allstack)>0:
					top.allstack.pop()
				while len(top.numstack)>0:
					top.numstack.pop()
				while len(top.operstack)>0:
					top.operstack.pop()


		else:#if operator button or number button was clicked

			if isinstance(self.oper,int):#for number buttons it just inserts the number to the rightmost of the expression in top box
				top.top_box.insert(len(top.allstack), self.oper)
				top.allstack.append(self.oper)
				print(top.allstack)


			else:
				top.top_box.insert(len(top.allstack),self.oper)
				top.allstack.append(self.oper)
				print(top.allstack)


	def precedence(op):
		if op=='+' or op=='-':
			return 1
		elif op=='x' or op=='/':
			return 2
		else:
			return -1

	def opers( operation ):
		
		if operation=='+':
			a =top.numstack.pop()
			b =top.numstack.pop()
			return a+b
		elif operation=='-':
			a =top.numstack.pop()
			b =top.numstack.pop()
			return b-a
		elif operation=='x':
			a =top.numstack.pop()
			b =top.numstack.pop()
			return a*b
		elif operation=='/':
			a =top.numstack.pop()
			b =top.numstack.pop()
			if a==0:
				top.d='error'
			else:
				return b/a
