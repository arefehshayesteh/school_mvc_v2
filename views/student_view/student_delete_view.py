import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from controllers.student_controller.student_delete_controller import StudentDeleteContoller

class StudentDeleteView(ttk.Frame):
     def __init__(self, master):
        super().__init__(master, padding= 10)
        self.pack(fill= BOTH, expand= True)
        cotroll = StudentDeleteContoller

        ttk.Label(self, text= "کدملی دانش اموزی را که میخواهید حذف کنید وارد کنید").pack(pady= 5)
        self.delete_entry = ttk.Entry(self)
        self.delete_entry.pack(pady= 5)
        self.delete_button= ttk.Button(self, text="حذف" ,bootstyle=SUCCESS)
        self.delete_button.pack(pady=10)
    
     def get_student_code(self):
        return self.delete_entry.get()
     
    
 