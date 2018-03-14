import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

def hit_me():
    # tk.messagebox.showinfo(title='Hi',message='hahhaha')
    # tk.messagebox.showwarning(title='Hi',message='NO')
    # tk.messagebox.showerror(title='Hi',message='ERROR')
    # print(tk.messagebox.askquestion(title='Hi',message='hahhaha') )# return 'yes' or 'no'
    # print(tk.messagebox.askyesno(title='Hi',message='hahhaha') )   #return 'True' or 'False'
    # print(tk.messagebox.askokcancel(title='Hi',message='hahhaha') )  #return 'True' or 'False
       print(tk.messagebox.askretrycancel(title='Hi',message='hahhaha') )  #return 'True' or 'False'
tk.Button(window,text='hit me',command=hit_me).pack()
window.mainloop()

