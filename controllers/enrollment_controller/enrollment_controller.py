from messages.errors import ErrorMessages
from tkinter import messagebox

class EnrollmentController:
    def __init__(self, model, view):
        self.model= model
        self.view= view
        self.view.reserch_button.config(command= self.reserch_form)

    def reserch_form(self):
        reserch_student= self.model.search_student_by_code()
        self.view.return_student_data(reserch_student)