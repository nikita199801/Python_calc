from tkinter import *
import test

def button_clicked():             #нажатие для клавиши равно
	test.vvod(entry.get())
	entry.delete(0,END)
	entry.insert(0,str(test.sum))
	
def close():
	root.destroy()
	root.quit()


root=Tk()                #Создаем форму
root.title("Calculator")
root.geometry("270x280")

entry=Entry(root, bd=5, width=15)          # Строка ввода
entry.grid(row=0, column=1, columnspan= 3)

Button_0 = Button(root, text='0', width=4, height= 2, bg='black', fg='white', font = "Arial 15", command=lambda: entry.insert(10,'0')).grid(row=5, column=1)        #кнопки..... 
Button_1 = Button(root, text='1', width=4, height= 2, bg='black', fg='white', font = "Arial 15", command=lambda: entry.insert(10,'1')).grid(row=4, column=0)
Button_2 = Button(root, text='2', width=4, height= 2, bg='black', fg='white', font = "Arial 15", command=lambda: entry.insert(10,'2')).grid(row=4, column=1)
Button_3 = Button(root, text='3', width=4, height= 2, bg='black', fg='white', font = "Arial 15", command=lambda: entry.insert(10,'3')).grid(row=4, column=2)
Button_4 = Button(root, text='4', width=4, height= 2, bg='black', fg='white', font = "Arial 15", command=lambda: entry.insert(10,'4')).grid(row=3, column=0)
Button_5 = Button(root, text='5', width=4, height= 2, bg='black', fg='white', font = "Arial 15", command=lambda: entry.insert(10,'5')).grid(row=3, column=1)
Button_6 = Button(root, text='6', width=4, height= 2, bg='black', fg='white', font = "Arial 15", command=lambda: entry.insert(10,'6')).grid(row=3, column=2)
Button_7 = Button(root, text='7', width=4, height= 2, bg='black', fg='white', font = "Arial 15", command=lambda: entry.insert(10,'7')).grid(row=2, column=0)
Button_8 = Button(root, text='8', width=4, height= 2, bg='black', fg='white', font = "Arial 15", command=lambda: entry.insert(10,'8')).grid(row=2, column=1)
Button_9 = Button(root, text='9', width=4, height= 2, bg='black', fg='white', font = "Arial 15", command=lambda: entry.insert(10,'9')).grid(row=2, column=2) 
Button_dot = Button(root, text='.', width=4, height= 2, bg='black', fg='white', font = "Arial 15", command=lambda: entry.insert(10,'.')).grid(row=5, column=0)
Button_is = Button(root, text='=', width=4, height= 2, bg='black', fg='white', font = "Arial 15", command=button_clicked).grid(row=5, column=2)
Button_plus = Button(root, text='+', width=4, height= 2, bg='black', fg='white', font = "Arial 15", command=lambda: entry.insert(10,'+')).grid(row=2, column=4)
Button_minus = Button(root, text='-', width=4, height= 2, bg='black', fg='white', font = "Arial 15", command=lambda: entry.insert(10,'-')).grid(row=3, column=4)
Button_muliply = Button(root, text='*', width=4, height= 2, bg='black', fg='white', font = "Arial 15", command=lambda: entry.insert(10,'*')).grid(row=4, column=4)
Button_divide = Button(root, text='/', width=4, height= 2, bg='black', fg='white', font = "Arial 15", command=lambda: entry.insert(10,'/')).grid(row=5, column=4)
Button_clear = Button(root, text='C', width=4, height= 2, bg='black', fg='white', font = "Arial 15", command=lambda: entry.delete(0,END)).grid(row=2, column=5)      #... конец кнопок

root.protocol('WM_DELETE_WINDOW', close)
root.mainloop()

