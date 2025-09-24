import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class LessonView(ttk.Frame):
    def __init__(self, master):
        super(). __init__(master, padding= 20)
        self.pack(fill= BOTH, expand= True)


        self.rowconfigure(0, weight= 1)
        self.rowconfigure(1, weight= 3)
        self.rowconfigure(2, weight= 1)
        self.columnconfigure(0, weight= 3)


        self.code_entry = ttk.Entry(self)
        self.code_entry.grid(column= 0,row= 0, sticky= EW, padx= 2, pady= 5)
        ttk.name_labal = ttk.Label(self, text= "کدملی دانش اموز را وارد کنید").grid(column= 1, row= 0, sticky= E, padx= 10, pady= 5)


    def get_student_code(self):
        return{
            "code" : self.code_entry.get()
        }
