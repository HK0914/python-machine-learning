import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

canvas = tk.Canvas(window, bg='green', height=100, width=200)
image_file = tk.PhotoImage(file='ins.gif')
image = canvas.create_image(10,10,anchor='nw',image=image_file)
x0, y0, x1, y1 = 50, 50, 80, 80
line=canvas.create_line(x0, y0, x1, y1)
oval = canvas.create_oval(x0, y0, x1, y1,fill='red')
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180,fill='orange')
rect = canvas.create_rectangle(100, 30, 100+20, 30+20,fill='yellow')
canvas.pack()

def moviet1():
    canvas.move(oval,1,1)

def moviet2():
    canvas.move(oval,-1,-1)

def moviet3():
    canvas.move(rect,0,2)
b1=tk.Button(window,text=' oval  right-downward ',command=moviet1).pack()
b2=tk.Button(window,text='oval  left-upward ',command=moviet2).pack()
b2=tk.Button(window,text='move rect',command=moviet3).pack()

window.mainloop()
