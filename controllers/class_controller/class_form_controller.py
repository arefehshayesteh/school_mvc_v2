from messages.errors import ErrorMessages
from tkinter import messagebox

class ClassFormController:
    def __init__(self, model , view):
        self.model = model
        self.view = view
        self.view.save_button.config(command=self.save_form)

    def save_form(self):
        try:
            data = self.view.get_class_form()
            self.model.add_class(data["name"], data["capacity"])
            raise ValueError(ErrorMessages.SUCCESSFUL_SUBMIT)
        except Exception as e:
            raise ValueError(ErrorMessages.UNSUCCESSFUL_SUBMIT)


    def get_classes(self):
        return self.model.get_all_classes()
