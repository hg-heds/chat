import tkinter as tk
from time import sleep
from tkinter import S,N,W,E,DISABLED,LEFT,END,NORMAL
RUNNING = True

palette = [
    '#f7faff',
    '#e4eefe',
    '#ffffff',
    '#7f8f05'
]

class APP:
    def __init__(self) -> None:
        self.RUNNING = True
        self.send_function = self._foo
        self.root = tk.Tk()
        self.root.resizable(0,0)
        self.root.geometry("700x700")
        self.root.title("Chat")
        self.root.protocol("WM_DELETE_WINDOW", self._onclosing)


        self.title_frame = tk.Frame(self.root, padx=10, pady=5, width=10, height=60, background=palette[0])
        self.title_frame.grid(row=0, column=0,columnspan=1, sticky=S+N+W+E)
        self.title_frame.grid_propagate(0)

        self.textbox_frame = tk.Frame(self.root, padx=10, pady=2, width=700, height=700,background=palette[0])
        self.textbox_frame.grid(row=1, column=0,columnspan=1, sticky=S+N+W+E)
        self.textbox_frame.grid_propagate(0)

        self.textbox = tk.Text(self.textbox_frame, padx=10, pady=2, width=82, height=35,background=palette[1],fg=palette[3])
        self.textbox.grid(row=0, column=0,columnspan=1, sticky=E)
        self.textbox.grid_propagate(0)
        self.textbox.config(state=DISABLED)

        self.insert_frame = tk.Frame(self.textbox_frame, pady=2, width=10, height=60,background=palette[0])
        self.insert_frame.grid(row=1, column=0, columnspan=1, sticky=W, pady=20)
        self.insert_frame.grid_propagate(0)

        self.insert = tk.Entry(self.insert_frame,width=105,background=palette[1])
        self.insert.pack(side=LEFT)

        self.insert.bind('<Return>',lambda x:self.ins())
        send_btn = tk.Button(self.insert_frame, width=5, height=1,text='->',command=lambda: self.ins(), bg=palette[1])
        send_btn.pack(side=LEFT)

        self.textbox.insert(END,'Hello\n')
        
    def _foo(self, message: str) -> None:
        print(message)

    def _onclosing(self) -> None:
        self.RUNNING = False 
        sleep(1.1)
        self.send_function('#')
        self.root.destroy()

    def start(self) -> None:
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            self.root.destroy()

    def running(self) -> bool:
        return self.RUNNING


    def ins(self,message: str|None = None) -> None:
        if not message:
            entry_value = self.insert.get()
            message = f"Você: {entry_value}"
            self.send_function(entry_value)
            self.insert.delete(0,END)

            if entry_value == '#':
                self._onclosing()
                return 
            
        self.textbox.config(state=NORMAL)
        self.textbox.insert(END,message+'\n')
        self.textbox.config(state=DISABLED)
        return 



if __name__ == '__main__':
    app = APP()
    app.start()