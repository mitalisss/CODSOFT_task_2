#simple calculator
from tkinter import *

#window
root=Tk()
root=root
root.title("CALCULATOR")
root.geometry("500x470")
root.configure(bg="grey15")
root.resizable(0,0)

#text display area
txt_display=Entry(root,font=('cambria',28,'bold'),bd=8,width=22,justify='right',background='ivory')
txt_display.grid(row=0,column=0,columnspan=4)

txt_display.delete(0,END)
operation=""
result=0

# function of buttons
def btn_click(number):
    txt_display.insert(END,str(number))

def btn_clear():
    txt_display.delete(0,END)

def btn_equals():
    result=str(eval(txt_display.get()))
    txt_display.delete(0,END)
    txt_display.insert(END,result)

# buttons
n_1=Button(root,font=('cambria',24,'bold',),text='1',width=6,height=2,bg="grey15",command=lambda:btn_click(1))
n_2=Button(root,font=('cambria',24,'bold'),text='2',width=6,height=2,bg="grey15",command=lambda:btn_click(2))
n_3=Button(root,font=('cambria',24,'bold'),text='3',width=6,height=2,bg="grey15",command=lambda:btn_click(3))
n_4=Button(root,font=('cambria',24,'bold'),text='4',width=6,height=2,bg="grey15",command=lambda:btn_click(4))
n_5=Button(root,font=('cambria',24,'bold'),text='5',width=6,height=2,bg="grey15",command=lambda:btn_click(5))
n_6=Button(root,font=('cambria',24,'bold'),text='6',width=6,height=2,bg="grey15",command=lambda:btn_click(6))
n_7=Button(root,font=('cambria',24,'bold'),text='7',width=6,height=2,bg="grey15",command=lambda:btn_click(7))
n_8=Button(root,font=('cambria',24,'bold'),text='8',width=6,height=2,bg="grey15",command=lambda:btn_click(8))
n_9=Button(root,font=('cambria',24,'bold'),text='9',width=6,height=2,bg="grey15",command=lambda:btn_click(9))
n_0=Button(root,font=('cambria',24,'bold'),text='0',width=6,height=2,bg="grey15",command=lambda:btn_click(0))
n_add=Button(root,font=('cambria',24,'bold'),text='+',width=6,height=2,bg="grey15",command=lambda:btn_click('+'))
n_subtract=Button(root,font=('cambria',24,'bold'),text='-',width=6,height=2,bg="grey15",command=lambda:btn_click('-'))
n_multiply=Button(root,font=('cambria',24,'bold'),text='*',width=6,height=2,bg="grey15",command=lambda:btn_click('*'))
n_divide=Button(root,font=('cambria',24,'bold'),text='/',width=6,height=2,bg="grey15",command=lambda:btn_click('/'))
n_clear=Button(root,font=('cambria',24,'bold'),text='C',width=6,height=2,bg="grey15",command=btn_clear)
n_equals=Button(root,font=('cambria',24,'bold'),text='=',width=6,height=2,bg="grey15",command=btn_equals)

#position of buttons
n_1.grid(row=1,column=0)
n_2.grid(row=1,column=1)
n_3.grid(row=1,column=2)

n_4.grid(row=2,column=0)
n_5.grid(row=2,column=1)
n_6.grid(row=2,column=2)

n_7.grid(row=3,column=0)
n_8.grid(row=3,column=1)
n_9.grid(row=3,column=2)

n_0.grid(row=4,column=0)
n_clear.grid(row=4,column=1)
n_equals.grid(row=4,column=2)

n_add.grid(row=1,column=3)
n_subtract.grid(row=2,column=3)
n_multiply.grid(row=3,column=3)
n_divide.grid(row=4,column=3)

#color of text of button
buttons=[n_1,n_2,n_3,n_4,n_5,n_6,n_7,n_8,n_9,n_0]
calbtn=[n_add,n_subtract,n_multiply,n_divide]

for button in buttons:
    button.configure(fg='white')

for btn in calbtn:
    btn.configure(fg='gold')

n_equals.config(fg="red")
n_clear.config(fg="red")

root.mainloop()
