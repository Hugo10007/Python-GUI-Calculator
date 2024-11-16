'''
Hugo Piper
Personal Project: Experimenting with TKinter module by creating a calculator.
14/11/2024
First year, first term of University.
'''
from tkinter import *

#Sets the 'root widget', a widget is the window that pops up.
root = Tk()
root.title("Hugo's Calculator")
root.resizable(False, False)
root.geometry("590x463")


#Make the bar at the top of the calculator where the numbers will be displayed.
calcEntry = Entry(root, width=50, borderwidth=5, state='readonly')
calcEntry.grid(padx=10, pady=10, column=0, row=0, columnspan=4)


def toggleEntryBox_decorator(func):
	def wrapper(*args):
		'''
		This is a decorator/wrapper function that toggles typing in the calculator window before and after a function is ran.
		This ensures the user cannot type inside the Entry window hhich could be a potential threat to the program. 
		'''
		calcEntry.config(state='normal')
		func(*args)
		calcEntry.config(state='readonly')
	return wrapper

@toggleEntryBox_decorator
def whenUserClicks(number):
	'''
	This function gets the number that the user entered and displays it on the calculator.
	'''
	currentEntry = calcEntry.get()
	calcEntry.delete(0, END)
	calcEntry.insert(0, str(currentEntry) + str(number))

@toggleEntryBox_decorator
def clear():
	'''
	This function deletes whats inside the calculators number screen when the user presses the "Clear" button. 
	'''
	calcEntry.delete(0, END)

@toggleEntryBox_decorator
def equals():
	#This function gets the results of what is entered in the Entry box.
	#It uses the Eval() function to convert the string into readabe code.
	#If the code throws an error, it is handled as an exception instead of crashing the software.
	
    try:
        # Get the current entry from the calculator
        result = calcEntry.get()
        # Evaluate the mathematical expression
        calculated_result = eval(result)
        # Clear the entry and display the result
        calcEntry.delete(0, END)
        calcEntry.insert(0, str(calculated_result))
    except Exception as e:
        # Handle any errors gracefully
        calcEntry.delete(0, END)
        calcEntry.insert(0, f"Error - {e} - Press ← to clear")
        print(f"An error occurred: {e}")


#Create instances of buttons
button1 = Button(root, text='1', padx=65, pady=30, background='#2e2e2e', foreground='#e2e2e2',command=lambda: whenUserClicks(1))
button2 = Button(root, text='2', padx=65, pady=30, background='#2e2e2e', foreground='#e2e2e2', command=lambda: whenUserClicks(2))
button3 = Button(root, text='3', padx=65, pady=30, background='#2e2e2e', foreground='#e2e2e2', command=lambda: whenUserClicks(3))
buttonMinus = Button(root, text='-', padx=65, pady=30, background='#4f4f4f', foreground='#e2e2e2', command=lambda: whenUserClicks('-'))

button4 = Button(root, text='4', padx=65, pady=30, background='#2e2e2e', foreground='#e2e2e2', command=lambda: whenUserClicks(4))
button5 = Button(root, text='5', padx=65, pady=30, background='#2e2e2e', foreground='#e2e2e2', command=lambda: whenUserClicks(5))
button6 = Button(root, text='6', padx=65, pady=30, background='#2e2e2e', foreground='#e2e2e2', command=lambda: whenUserClicks(6))
buttonMultiply = Button(root, text='*', padx=65, pady=30, background='#4f4f4f', foreground='#e2e2e2', command=lambda: whenUserClicks('*'))

button7 = Button(root, text='7', padx=65, pady=30, background='#2e2e2e', foreground='#e2e2e2', command=lambda: whenUserClicks(7))
button8 = Button(root, text='8', padx=65, pady=30, background='#2e2e2e', foreground='#e2e2e2', command=lambda: whenUserClicks(8))
button9 = Button(root, text='9', padx=65, pady=30, background='#2e2e2e', foreground='#e2e2e2', command=lambda: whenUserClicks(9))
buttonDivide = Button(root, text='÷', padx=63, pady=30, background='#4f4f4f', foreground='#e2e2e2', command=lambda: whenUserClicks('/'))

buttonClear = Button(root, text='←', padx=62, pady=30, background='#4f4f4f', foreground='#e2e2e2', command=clear)
button0 = Button(root, text='0', padx=65, pady=30, background='#2e2e2e', foreground='#e2e2e2', command=lambda: whenUserClicks(0))
buttonDecimal = Button(root, text='.', padx=67, pady=30, background='#4f4f4f', foreground='#e2e2e2', command=lambda: whenUserClicks('.'))
buttonAddition = Button(root, text='+', padx=63, pady=30, background='#4f4f4f', foreground='#e2e2e2', command=lambda: whenUserClicks('+'))

buttonEquals = Button(root, text='=', padx=138, pady=3, background='#368ab3', foreground='#e2e2e2', command=equals)
buttonOpenBracket = Button(root, text='(', padx=66, pady=3, background='#2e2e2e', foreground='#e2e2e2', command=lambda: whenUserClicks('('))
buttonCloseBracket = Button(root, text=')', padx=66, pady=3, background='#2e2e2e', foreground='#e2e2e2', command=lambda: whenUserClicks(')'))


#Position buttons within the calculator
button7.grid(row=1, column=1)
button8.grid(row=1, column=2)
button9.grid(row=1, column=3)
buttonDivide.grid(row=1, column=4)

button4.grid(row=2, column=1)
button5.grid(row=2, column=2)
button6.grid(row=2, column=3)
buttonMultiply.grid(row=2, column=4)

button1.grid(row=3, column=1)
button2.grid(row=3, column=2)
button3.grid(row=3, column=3)
buttonMinus.grid(row=3, column=4)

buttonClear.grid(row=4, column=1)
button0.grid(row=4, column=2)
buttonDecimal.grid(row=4, column=3)
buttonAddition.grid(row=4, column=4)

buttonEquals.grid(row=5, column=0, columnspan=3)
buttonOpenBracket.grid(row=5, column=3)
buttonCloseBracket.grid(row=5, column=4)


#This is an event loop, it loops the GUI over and over to wait for updates (if buttons are pressed, where the mouse is located..etc)
#The event loop is required to run and display the GUI.
root.mainloop()