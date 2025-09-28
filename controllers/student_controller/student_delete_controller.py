from messages.errors import ErrorMessages

class StudentDeleteContoller():
    def __init__(self, student_model,   view):
        self.student_model = student_model
        self.view = view

        self.view.delete_button.config(command=self.delete_student)

    def delete_student(self):
        code = self.view.get_student_code()
        # if len(code) != 10:
        #     raise ValueError(ErrorMessages.INVALID_CODE)
        # if not code.isdigit():
        #     raise ValueError(ErrorMessages.CODE_NOT_INTIGER)
        
        student = self.student_model.search_student_by_code(code)
        if not student:
            self.show_message("دانش‌آموزی با این کد ملی پیدا نشد.")
            return
        self.student_model.delete_student_by_code(code)
        self.show_message("دانش‌آموز با موفقیت حذف شد.")

    def show_message(self, message):
        print(message)
        
