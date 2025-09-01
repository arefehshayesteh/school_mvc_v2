import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox


class ClassView(ttk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.name_entry = ttk.Entry(self)
        self.name_entry.pack(pady=5)

        self.capacity_entry = ttk.Entry(self)
        self.capacity_entry.pack(pady=5)

        add_btn = ttk.Button(self, text="افزودن کلاس", command=self.add_class)
        add_btn.pack(pady=5)
        register_btn = ttk.Button(self, text="ثبت‌نام دانش‌آموز", command=self.open_register_window)
        register_btn.pack(pady=5)
        

        self.class_list = ttk.Treeview(self, columns=("id", "name", "capacity"), show="headings")
        self.class_list.heading("id", text="ID")
        self.class_list.heading("name", text="نام کلاس")
        self.class_list.heading("capacity", text="ظرفیت")
        self.class_list.pack(fill="both", expand=True)

        self.refresh_class_list()

    def add_class(self):
        name = self.name_entry.get()
        try:
            capacity = int(self.capacity_entry.get())
            self.controller.create_class(name, capacity)
            self.refresh_class_list()
        except Exception as e:
            Messagebox.show_error(title="خطا", message=str(e))

    def refresh_class_list(self):
        for row in self.class_list.get_children():
            self.class_list.delete(row)
        for cls in self.controller.get_classes():
            self.class_list.insert("", "end", values=cls)

    def open_register_window(self):
        import tkinter as tk
        from models.student_model import StudentModel
        from controllers.student_controller import studentController
        from views.student_view import studentView

        db = self.controller.model.db #؟؟
        student_model = StudentModel(db)
        student_controller = studentController(student_model)

        student_window = tk.Toplevel(self)
        student_window.title("ثبت‌نام دانش‌آموز")
        student_window.geometry("600x400")

        studentView(student_window, student_controller)


