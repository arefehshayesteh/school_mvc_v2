from messages.errors import ErrorMessages
from PyQt5.QtWidgets import QMessageBox

class StudentFormController:
    def __init__(self, model , view):
        self.model = model
        self.view = view
        self.view.save_button.config(command=self.save_form)

    def save_form(self):
        try:
            data = self.view.get_student_form()
            self.model.add_student(data["name"], data["code"], data["mobile"], data["password"])
            self.show_message(ErrorMessages.SUCCESSFUL_SUBMIT)
        except Exception as e:
            self.show_message(ErrorMessages.UNSUCCESSFUL_SUBMIT)

    def get_students(self):
        return self.model.get_all_students()


    def show_message(self, message):
        print(message)



    