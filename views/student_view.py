import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox

class studentView(ttk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):

        self.name_entry = ttk.Entry(self)
        self.name_entry.pack(pady=5)

        self.code_entry = ttk.Entry(self)
        self.code_entry.pack(pady=5)

        self.mobile_entry = ttk.Entry(self)
        self.mobile_entry.pack(pady=5)
        
        self.password_entry = ttk.Entry(self)
        self.password_entry.pack(pady=5)

        add_btn = ttk.Button(self, text="ثبت نام ", command=self.add_student)
        add_btn.pack(pady=5)

        self.student_list = ttk.Treeview(self, columns=("id", "name", "code", "mobile", "password"), show="headings")
        self.student_list.heading("id", text="ID")
        self.student_list.heading("name", text="نام دانش اموز")
        self.student_list.heading("code", text="کدملی")
        self.student_list.heading("mobile", text="شماره تلفن")
        self.student_list.heading("password", text="رمز عبور")
     
        self.student_list.pack(fill="both", expand=True)

        self.refresh_student_list()

    def add_student(self):
        name = self.name_entry.get()
        code = self.code_entry.get()
        monile = self.mobile_entry.get()
        password = self.password_entry.get()
        try:
            self.controller.register_student(name, code, monile, password)
            self.refresh_student_list()
        except Exception as e:
            Messagebox.show_error(title="خطا", message=str(e))

    def refresh_student_list(self):
        for row in self.student_list.get_children():
            self.student_list.delete(row)
        for cls in self.controller.get_students():
            self.student_list.insert("", "end", values=cls)
