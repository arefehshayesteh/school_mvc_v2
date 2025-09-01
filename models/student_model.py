class StudentModel:
    def __init__(self, db):
        self.db = db

    def add_student(self, name, code):
        self.db.execute("INSERT INTO students (name, code ) VALUES (? , ?)", (name, code ))

    def get_all_students(self):
        return self.db.fetchall("SELECT id, name, code FROM students")

    def delete_student(self, student_id):
        self.db.execute("DELETE FROM students WHERE id = ?", (student_id,))
