import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class EnrollmentView(ttk.Frame):
    def __init__(self, master):
        super(). __init__(master, padding= 20)
        self.pack(fill= BOTH, expand= True)
        self.class_vars = []

        ttk.Label(self, text= "کدملی دانش اموز را وارد کنید").pack(pady= 5)
        self.code_entry = ttk.Entry(self)
        self.code_entry.pack(pady= 5)
        self.reserch_button= ttk.Button(self, text="جستجو")
        self.reserch_button.pack(pady=5)

        self.name_label = ttk.Label(self, text="")
        self.name_label.pack(pady=5)
        self.mobile_label = ttk.Label(self, text="")
        self.mobile_label.pack(pady=5)

        self.class_frame = ttk.Frame(self)
        self.class_frame.pack(pady=10, fill=X)

        self.enroll_button= ttk.Button(self, text="ثبت" ,bootstyle=SUCCESS)
        self.enroll_button.pack(pady=10)


    def get_student_code(self):
        return self.code_entry.get()
        
    
    def student_data(self, name , mobile):
        self.name_label.config(text=f"دانش‌آموز: {name}")
        self.mobile_label.config(text=f"موبایل: {mobile}")


    def class_data(self, classes, enrolled_ids=None):
        enrolled_ids = enrolled_ids or []
        for i in self.class_frame.winfo_children():
            i.destroy()
        self.class_vars.clear()
        for c_id, title in classes:
            var = ttk.BooleanVar(value=(c_id in enrolled_ids))
            chk = ttk.Checkbutton(self.class_frame, text= title, variable= var)
            chk.pack(anchor=W)
            self.class_vars.append((c_id, var))

    def get_selected_classes(self):
        return [c_id for c_id, var in self.class_vars if var.get()]
        
