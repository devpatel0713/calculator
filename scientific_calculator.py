from tkinter import*
import math
#import parser
import tkinter.messagebox

root = Tk()
root.title("Standard Calculator")
root.resizable(width= False, height = False)
root.geometry("400x400+460+40")


txtResult = Entry(font = ('arial', 16,'bold'),bg="black", bd = 30, width = 26 , justify=RIGHT)
txtResult.grid(row = 0, column= 0, columnspan= 4, pady = 1)

scientific_buttons = []


def click(num):
    temp = str(txtResult.get())
    num = temp + str(num)
    txtResult.delete(0,END)
    txtResult.insert(END, num)
def clear():
    txtResult.delete(0,END)
def backspace():
    temp = txtResult.get()
    txtResult.delete(0,END)
    txtResult.insert(0, temp[0, -1])

def answer():
    temp = str(txtResult.get())
    ans = eval(temp)
    txtResult.delete(0,END)
    txtResult.insert(END, ans)

def scientific_evaluate(operation):
    try:
        number = float(txtResult.get())
        txtResult.delete(0, END)
        
        if operation == 'sin':
            result = math.sin(math.radians(number))
        elif operation == 'cos':
            result = math.cos(math.radians(number))
        elif operation == 'tan':
            result = math.tan(math.radians(number))
        elif operation == 'log':
            result = math.log10(number)
        elif operation == 'pi':
            result = math.pi
        elif operation == 'exp':
            result = math.exp(number)
        elif operation == 'sinh':
            result = math.sinh(math.radians(number))
        elif operation == 'tanh':
            result= math.tanh(math.radians(number))
        elif operation == 'cosh':
            result= math.cosh(math.radians(number))
        elif operation == '2pi':
            result= math.tau
        elif operation == 'e':
            result= math.e
        elif operation == 'exp':
            result= math.exp(number)
        elif operation == 'log':
            result= math.log(number)
        elif operation == 'asinh':
            result= math.asinh(number)
        elif operation == 'acosh':
            result= math.acosh(number)
        elif operation == 'deg':
            result= math.degrees(number)
        elif operation == 'log2':
            result= math.log2(number)
        elif operation == 'lgamma':
            result= math.lgamma(number)
        elif operation == 'expm1':
            result= math.expm1(number)
        elif operation == 'log1p':
            result= math.log1p(number)
        elif operation == 'log10':
            result= math.log10(number)
        else:
            result = "Error"
        
        txtResult.insert(END, result)
    except Exception as e:
        txtResult.delete(0, END)
        txtResult.insert(END, "Error")
#Standard Calculator Buttons
#Row 1       
btn_ac = Button(text = "AC", width = 6, height = 2 , font = ('arial', 16, 'bold'), bd = 4, bg = "black", command = clear).grid(row = 2, column= 0, pady = 1)
btn_plus_mius = Button(text = "+/-", width = 6, height = 2 , font = ('arial', 16, 'bold'), bd = 4, bg = "black", command = lambda : click("-")).grid(row = 2, column= 1, pady = 1)
btn_mod = Button(text = "%", width = 6, height = 2 , font = ('arial', 16, 'bold'), bd = 4, bg = "black",command = lambda : click("mod")).grid(row = 2, column= 2, pady = 1)
btn_backspace = Button( text = "⌫", width =6, height = 2, font = ('arial', 16, 'bold'), bd = 4, bg = "black", command = backspace).grid(row = 2, column= 3, pady = 1)

#Row 2
btn_7 = Button(text = "7", width = 6, height = 2 , font = ('arial', 16, 'bold'), bd = 4, bg = "black",command = lambda : click("7")).grid(row = 3, column= 0, pady = 1)
btn_8 = Button(text = "8", width = 6, height = 2 , font = ('arial', 16, 'bold'), bd = 4, bg = "black",command = lambda : click("8")).grid(row = 3, column= 1, pady = 1)
btn_9 = Button(text = "9", width = 6, height = 2 , font = ('arial', 16, 'bold'), bd = 4, bg = "black",command = lambda : click("9")).grid(row = 3, column= 2, pady = 1)
btn_mult = Button(text = "*", width = 6, height = 2 , font = ('arial', 16, 'bold'), bd = 4, bg = "black", command = lambda : click("*")).grid(row = 3, column= 3, pady = 1)

#Row 3
btn_4 = Button(text = "4", width = 6, height = 2 , font = ('arial', 16, 'bold'), bd = 4, bg = "black", command = lambda : click("4")).grid(row = 4, column= 0, pady = 1)
btn_5 = Button(text = "5", width = 6, height = 2 , font = ('arial', 16, 'bold'), bd = 4, bg = "black", command = lambda : click("5")).grid(row = 4, column= 1, pady = 1)
btn_6 = Button(text = "6", width = 6, height = 2 , font = ('arial', 16, 'bold'), bd = 4, bg = "black", command = lambda : click("6")).grid(row = 4, column= 2, pady = 1)
btn_sub = Button(text = "-", width = 6, height = 2 , font = ('arial', 16, 'bold'), bd = 4, bg = "black", command = lambda : click("-")).grid(row = 4, column= 3, pady = 1)

#Row 4
btn_1 = Button(text = "1", width = 6, height = 2 , font = ('arial', 16, 'bold'), bd = 4, bg = "black", command = lambda : click("1")).grid(row = 5, column= 0, pady = 1)
btn_2 = Button(text = "2", width = 6, height = 2 , font = ('arial', 16, 'bold'), bd = 4, bg = "black", command = lambda : click("2")).grid(row = 5, column= 1, pady = 1)
btn_3 = Button(text = "3", width = 6, height = 2 , font = ('arial', 16, 'bold'), bd = 4, bg = "black", command = lambda : click("3")).grid(row = 5, column= 2, pady = 1)
btn_add = Button(text = "+", width = 6, height = 2 , font = ('arial', 16, 'bold'), bd = 4, bg = "black", command = lambda : click("+")).grid(row = 5, column= 3, pady = 1)

#Row 5
btn_0 = Button(text = "0", width = 6, height = 2 , font = ('arial', 16, 'bold'), bd = 4, bg = "black", command = lambda : click("0")).grid(row = 6, column= 0, pady = 1)
btn_dec =Button(text = ".", width = 6, height = 2 , font = ('arial', 16, 'bold'), bd = 4, bg = "black", command = lambda : click(".")).grid(row = 6, column= 1, pady = 1)
btn_equal = Button(text = "=", width = 6, height = 2 , font = ('arial', 16, 'bold'), bd = 4, bg = "black", command = answer).grid(row = 6, column= 2, pady = 1)
btn_div = Button(text = "/", width = 6, height = 2 , font = ('arial', 16, 'bold'), bd = 4, bg = "black", command = lambda : click("/")).grid(row = 6, column= 3, pady = 1)

##Scientific Calculator Buttons


def IExit():
    IExit = tkinter.messagebox.askyesno("Scientific Calculator", "Confirm if you want to exit")
    if IExit > 0:
        root.destroy()
        return 

def add_scientific_buttons():
    global scientific_buttons
    #Row 1
    scientific_buttons = [
    Button( text = "sin", width=6,height = 2, font = ('arial', 16,'bold'), bd = 4, bg = "cadetblue", command = lambda : scientific_evaluate('sin')),
    Button( text = "tan", width=6,height = 2, font = ('arial', 16,'bold'), bd = 4, bg = "cadetblue", command = lambda : scientific_evaluate('tan')),
    Button( text = "cos", width=6,height = 2, font = ('arial', 16,'bold'), bd = 4, bg = "cadetblue", command = lambda : scientific_evaluate('cos')),
    Button( text = "π", width=6,height = 2, font = ('arial', 16,'bold'), bd = 4, bg = "cadetblue", command = lambda : click(math.pi)),
    #Row 2
    Button( text = "sinh", width=6,height = 2, font = ('arial', 16,'bold'), bd = 4, bg = "cadetblue", command = lambda : scientific_evaluate('sinh')),
    Button( text = "tanh", width=6,height = 2, font = ('arial', 16,'bold'), bd = 4, bg = "cadetblue", command = lambda : scientific_evaluate('tanh')),
    Button( text = "cosh", width=6,height = 2, font = ('arial', 16,'bold'), bd = 4, bg = "cadetblue", command = lambda : scientific_evaluate('cosh')),
    Button(text = "2π", width=6,height = 2, font = ('arial', 16,'bold'), bd = 4, bg = "cadetblue", command = lambda : click(math.tau)),
    #Row 3
    Button( text = "e", width=6,height = 2, font = ('arial', 16,'bold'), bd = 4, bg = "cadetblue", command = lambda : click(math.e)),
    Button( text = "mod", width=6,height = 2, font = ('arial', 16,'bold'), bd = 4, bg = "cadetblue", command = lambda : click('%')),
    Button( text = "exp", width=6,height = 2, font = ('arial', 16,'bold'), bd = 4, bg = "cadetblue", command = lambda : scientific_evaluate('exp')),
    Button( text = "log", width=6,height = 2, font = ('arial', 16,'bold'), bd = 4, bg = "cadetblue", command = lambda : scientific_evaluate('log')),
    #Row 4
    Button( text = "asinh", width=6,height = 2, font = ('arial', 16,'bold'), bd = 4, bg = "cadetblue", command = lambda : scientific_evaluate('asinh')),
    Button( text = "acosh", width=6,height = 2, font = ('arial', 16,'bold'), bd = 4, bg = "cadetblue", command = lambda : scientific_evaluate('acosh')),
    Button( text = "deg", width=6,height = 2, font = ('arial', 16,'bold'), bd = 4, bg = "cadetblue", command = lambda : scientific_evaluate('deg')),
    Button( text = "log2", width=6,height = 2, font = ('arial', 16,'bold'), bd = 4, bg = "cadetblue", command = lambda : scientific_evaluate('log2')),
    #Row 5
    Button( text = "lgamma", width=6,height = 2, font = ('arial', 16,'bold'), bd = 4, bg = "cadetblue", command = lambda : scientific_evaluate('lgamma')),
    Button( text = "expm1", width=6,height = 2, font = ('arial', 16,'bold'), bd = 4, bg = "cadetblue", command = lambda : scientific_evaluate('expm1')),
    Button( text = "log1p", width=6,height = 2, font = ('arial', 16,'bold'), bd = 4, bg = "cadetblue", command = lambda : scientific_evaluate('log1p')),
    Button(text = "log10", width=6,height = 2, font = ('arial', 16,'bold'), bd = 4, bg = "cadetblue", command = lambda : scientific_evaluate('log10')),
    ]
    for i, button in enumerate(scientific_buttons):
        button.grid(row = 2 + ( i // 4), column = 4 + (i % 4 ), padx= 5, pady = 1)
def remove_scientific():
    global scientific_buttons
    for button in scientific_buttons:
        button.grid_remove()
    scientific_buttons.clear()

def Scientific():
    add_scientific_buttons()
    root.title("Scientific Calculator")
    root.geometry("796x400+460+40")
    root.resizable(width = False, height = False)
    txtResult.config(width = 54)
    txtResult.grid(columnspan= 8)
    txtResult.delete(0, END)

def Standard():
   remove_scientific()
   root.title("Standard Calculator")
   root.resizable(width= False, height = False)
   root.geometry("400x400+460+40")
   txtResult.config(width = 26)
   txtResult.grid(columnspan= 4)
   txtResult.delete(0, END)

menu_bar = Menu(root)
filemenu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "Standard", command = Standard)
filemenu.add_separator()
filemenu.add_command(label = "Scientific", command = Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit",command = IExit)


root.config(menu = menu_bar)
root.mainloop()
