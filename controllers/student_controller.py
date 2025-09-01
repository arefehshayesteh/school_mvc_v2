from messages.errors import ErrorMessages

class studentController:
    def __init__(self, model):
        self.model = model

    def register_student(self, name, code):
       if not name:
           raise ValueError(ErrorMessages.INVALID_STUDENT_NAME)
       if not name.isalpha():
            raise ValueError(ErrorMessages.IF_NOT_WORD)
       if not code:
           raise ValueError(ErrorMessages.INVALID_CODE_NAME)
       
       if not code.isdigit():
            raise ValueError(ErrorMessages.CODE_NOT_INTIGER) 

       if len(code) != 10:
            raise ValueError(ErrorMessages.INVALID_CODE)

       self.model.add_student(name, code)

    def get_students(self):
        return self.model.get_all_students()