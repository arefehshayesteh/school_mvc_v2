class StudentModel:
    def __init__(self, db):
        self.db = db

    def add_student(self, name, code, mobile, password):
        self.db.execute("INSERT INTO students (name, code, mobile, password ) VALUES (? , ? , ? , ?)", (name, code, mobile, password))

    def get_all_students(self):
        return self.db.fetchall("SELECT * FROM students")

    def delete_student(self, student_id):
        self.db.execute("DELETE FROM students WHERE id = ?", (student_id,))

    def search_student_by_code(self, code):
        return self.db.fetchone("SELECT id, name, mobile FROM students WHERE code = ?", (code,))
   

