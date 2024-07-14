from tkinter import *
root=Tk()
root.title("Calculator")
root.geometry('400x350')
root.resizable(False,False)
root.configure(bg="light blue")

expression=" "

def show(value):
    global expression
    expression+=value
    label_result.config(text=expression)
def clear():
    global expression
    expression=" "
    label_result.config(text=expression)
def result():
    global expression
    result=" "
    if expression!=" ":
        result=eval(expression)
    else:
        result="error"
        expression=" "

    label_result.config(text=result)
def delete():
    global expression
    expression=expression[:-1]
    label_result.config(text=expression)



label_result=Label(root,width=17,height=2,bg="pink",text=" ",font=("areal",30))
label_result.place(x=0,y=0)
Button(root,text="C",bg="white",width=12,height=2,command=lambda:clear()).place(x=3,y=100)
Button(root,text="/",bg="white",width=12,height=2,command=lambda:show("/")).place(x=100,y=100)
Button(root,text="%",bg="white",width=12,height=2,command=lambda:show("%")).place(x=200,y=100)
Button(root,text="*",bg="white",width=12,height=2,command=lambda:show("*")).place(x=300,y=100)

Button(root,text="7",bg="white",width=12,height=2,command=lambda:show("7")).place(x=3,y=150)
Button(root,text="8",bg="white",width=12,height=2,command=lambda:show("8")).place(x=100,y=150)
Button(root,text="9",bg="white",width=12,height=2,command=lambda:show("9")).place(x=200,y=150)
Button(root,text="-",bg="white",width=12,height=2,command=lambda:show("-")).place(x=300,y=150)

Button(root,text="4",bg="white",width=12,height=2,command=lambda:show("4")).place(x=3,y=200)
Button(root,text="5",bg="white",width=12,height=2,command=lambda:show("5")).place(x=100,y=200)
Button(root,text="6",bg="white",width=12,height=2,command=lambda:show("6")).place(x=200,y=200)
Button(root,text="+",bg="white",width=12,height=2,command=lambda:show("+")).place(x=300,y=200)

Button(root,text="1",bg="white",width=12,height=2,command=lambda:show("1")).place(x=3,y=250)
Button(root,text="2",bg="white",width=12,height=2,command=lambda:show("2")).place(x=100,y=250)
Button(root,text="3",bg="white",width=12,height=2,command=lambda:show("3")).place(x=200,y=250)
Button(root,text="delete",bg="white",width=12,height=2,command=lambda:delete()).place(x=300,y=250)

Button(root,text="0",bg="white",width=26,height=2,command=lambda:show("0")).place(x=3,y=300)
Button(root,text=".",bg="white",width=12,height=2,command=lambda:show(".")).place(x=200,y=300)
Button(root,text="=",bg="white",width=12,height=2,command=lambda:result()).place(x=300,y=300)

root.mainloop()
