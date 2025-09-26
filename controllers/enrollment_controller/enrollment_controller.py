from messages.errors import ErrorMessages
from tkinter import messagebox

class EnrollmentController:
    def __init__(self, student_model, class_model, enrollment_model, view):
        self.student_model = student_model
        self.class_model = class_model
        self.enrollment_model = enrollment_model
        self.view = view
        self.student_id = None

        self.view.reserch_button.config(command=self.reserch_form)
        self.view.enroll_button.config(command=self.enroll_classes)

    def reserch_form(self):
        code = self.view.get_student_code()
        if len(code) != 10:
            ValueError(ErrorMessages.INVALID_CODE)
            return
        if not code.isdigit():
            ValueError(ErrorMessages.CODE_NOT_INTIGER)
            return

        student = self.student_model.search_student_by_code(code)
        if student:
            self.student_id = student[0]
            self.view.student_data(student[1], student[2])
            classes = self.class_model.get_all_classes()
            enrolled_ids = self.enrollment_model.get_enrolled_class_ids(self.student_id)
            self.view.class_data(classes, enrolled_ids)
        else:
            ValueError(ErrorMessages.STUDENT_NOT_FOUND)
    
    def enroll_classes(self):
        if not self.student_id:
            ValueError(ErrorMessages.STUDENT_NOT_SELECTED)
            return
        selected = self.view.get_selected_classes()
        self.enrollment_model.update_student_enrollments(self.student_id, selected)
        ValueError(ErrorMessages.UPDATE_SUBMIT)
