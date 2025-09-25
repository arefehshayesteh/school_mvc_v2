import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class EnrollmentView(ttk.Frame):
    def __init__(self, master):
        super(). __init__(master, padding= 20)
        self.pack(fill= BOTH, expand= True)


        ttk.Label(self, text= "کدملی دانش اموز را وارد کنید").pack(pady= 5)
        self.code_entry = ttk.Entry(self)
        self.code_entry.pack(pady= 5)

        self.name_label = ttk.Label(self, text="")
        self.name_label.pack(pady=5)
        self.mobile_label = ttk.Label(self, text="")
        self.mobile_label.pack(pady=5)

        self.class_frame = ttk.Frame(self)
        self.class_frame.pack(pady=10, fill=X)

        self.reserch_button= ttk.Button(self.navbar, text="جستجو" , command= self.return_student_data).pack(side=RIGHT , padx=1)
        self.reserch_button= ttk.Button(self.navbar, text="ثبت" , command= self.register_data).pack(side=RIGHT , padx=1)




    def get_student_code(self):
        return self.code_entry.get()
        
    
    def return_student_data(self, name , mobile):
        self.student_label.config(text=f"دانش‌آموز: {name}")
        self.mobile_label.config(text=f"موبایل: {mobile}")


    def register_data(self):
        pass
