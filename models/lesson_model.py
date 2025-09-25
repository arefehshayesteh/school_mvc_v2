class LessonModel:
    def __init__(self, db):
        self.db = db 

    def search_student_by_code(self, code):
        return self.db.fetchall("SELECT * FROM student WHERE code = ?", (code))
