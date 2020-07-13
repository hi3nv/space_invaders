from tkinter import *

def click(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def clear():
    global operator
    operator = ""
    text_input.set("")


def equal():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""


calculator = Tk()
calculator.title("Calculator")
operator = ""
text_input = StringVar()

text_display = Entry(calculator, font=('Helvetica', 15, 'bold'), textvariable=text_input, bd=30, insertwidth=4, bg="powder blue", justify="right").grid(columnspan=4)

# 7 to addition
button_7 = Button(calculator, padx=10, pady=10, bd=8, fg="black", font=('Helvectica', 15, 'bold'), text="7", bg="white", command=lambda:click(7)).grid(row=1, column=0)
button_8 = Button(calculator, padx=10, pady=10, bd=8, fg="black", font=('Helvectica', 15, 'bold'), text="8", bg="white", command=lambda:click(8)).grid(row=1, column=1)
button_9 = Button(calculator, padx=10, pady=10, bd=8, fg="black", font=('Helvectica', 15, 'bold'), text="9", bg="white", command=lambda:click(9)).grid(row=1, column=2)
button_addition = Button(calculator, padx=10, pady=10, bd=8, fg="black", font=('Helvectica', 15, 'bold'), text="+", bg="white", command=lambda:click('+')).grid(row=1, column=3)

# 4 to subtraction
button_4 = Button(calculator, padx=10, pady=10, bd=8, fg="black", font=('Helvectica', 15, 'bold'), text="4", bg="white", command=lambda:click(4)).grid(row=2, column=0)
button_5 = Button(calculator, padx=10, pady=10, bd=8, fg="black", font=('Helvectica', 15, 'bold'), text="5", bg="white", command=lambda:click(5)).grid(row=2, column=1)
button_6 = Button(calculator, padx=10, pady=10, bd=8, fg="black", font=('Helvectica', 15, 'bold'), text="6", bg="white", command=lambda:click(6)).grid(row=2, column=2)
button_subtraction = Button(calculator, padx=10, pady=10, bd=8, fg="black", font=('Helvectica', 15, 'bold'), text="-", bg="white", command=lambda:click('-')).grid(row=2, column=3)

# 1 to multiply
button_1 = Button(calculator, padx=10, pady=10, bd=8, fg="black", font=('Helvectica', 15, 'bold'), text="1", bg="white", command=lambda:click(1)).grid(row=3, column=0)
button_2 = Button(calculator, padx=10, pady=10, bd=8, fg="black", font=('Helvectica', 15, 'bold'), text="2", bg="white", command=lambda:click(2)).grid(row=3, column=1)
button_3 = Button(calculator, padx=10, pady=10, bd=8, fg="black", font=('Helvectica', 15, 'bold'), text="3", bg="white", command=lambda:click(3)).grid(row=3, column=2)
button_multiply = Button(calculator, padx=10, pady=10, bd=8, fg="black", font=('Helvectica', 15, 'bold'), text="*", bg="white", command=lambda:click('*')).grid(row=3, column=3)

# 0 to divide
button_0 = Button(calculator, padx=10, pady=10, bd=8, fg="black", font=('Helvectica', 15, 'bold'), text="0", bg="white", command=lambda:click(4)).grid(row=4, column=0)
button_clear = Button(calculator, padx=10, pady=10, bd=8, fg="black", font=('Helvectica', 15, 'bold'), text="C", bg="white", command=clear).grid(row=4, column=1)
button_equal = Button(calculator, padx=10, pady=10, bd=8, fg="black", font=('Helvectica', 15, 'bold'), text="=", bg="white", command=equal).grid(row=4, column=2)
button_divide = Button(calculator, padx=10, pady=10, bd=8, fg="black", font=('Helvectica', 15, 'bold'), text="/", bg="white", command=lambda:click('/')).grid(row=4, column=3)
calculator.mainloop()