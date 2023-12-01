import tkinter as tk
from time import sleep
from tkinter import S,N,W,E,DISABLED, LEFT, END,NORMAL
RUNNING = True

class APP:
    def __init__(self) -> None:
        self.RUNNING = True
        self.send_function = self.foo
        self.root = tk.Tk()
        self.root.resizable(0,0)
        self.root.geometry("700x700")
        self.root.title("Chat")
        self.root.protocol("WM_DELETE_WINDOW", self.onclosing)


        self.title_frame = tk.Frame(self.root, padx=10, pady=5, width=10, height=60)
        self.title_frame.grid(row=0, column=0,columnspan=1, sticky=S+N+W+E)
        self.title_frame.grid_propagate(0)

        self.textbox_frame = tk.Frame(self.root, padx=10, pady=2, width=690, height=700)
        self.textbox_frame.grid(row=1, column=0,columnspan=1, sticky=S+N+W+E)
        self.textbox_frame.grid_propagate(0)

        self.textbox = tk.Text(self.textbox_frame, padx=10, pady=2, width=90, height=35,background='bisque')
        self.textbox.grid(row=0, column=0,columnspan=1, sticky=E)
        self.textbox.grid_propagate(0)
        self.textbox.config(state=DISABLED)

        self.insert_frame = tk.Frame(self.textbox_frame, pady=2, width=10, height=60)
        self.insert_frame.grid(row=1, column=0, columnspan=1, sticky=W, pady=20)
        self.insert_frame.grid_propagate(0)

        self.insert = tk.Entry(self.insert_frame,width=105)
        self.insert.pack(side=LEFT)

        self.insert.bind('<Return>',lambda x:self.ins())
        send_btn = tk.Button(self.insert_frame, width=5, height=1,text='->',command=lambda: self.ins())
        send_btn.pack(side=LEFT)

        self.textbox.insert(END,'Hello\n')


    def start(self):
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            self.root.destroy()
        
    def foo(self, message):
        pass

    def onclosing(self):
        self.RUNNING = False 
        sleep(1.1)
        self.send_function('#')
        self.root.destroy()

    def running(self):
        return self.RUNNING


    def ins(self,message=None):
        if not message:
            entry_value = self.insert.get()
            message = f"Você: {entry_value}"
            self.send_function(entry_value)
            self.insert.delete(0,END)

            if entry_value == '#':
                self.RUNNING = False 
                sleep(1.1)
                self.onclosing()
                return
            
        self.textbox.config(state=NORMAL)
        self.textbox.insert(END,message+'\n')
        self.textbox.config(state=DISABLED)



if __name__ == '__main__':
    APP()