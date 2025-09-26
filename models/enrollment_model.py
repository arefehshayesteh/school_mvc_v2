class EnrollmentModel:
    def __init__(self, db):
        self.db = db

    def get_enrolled_class_ids(self, student_id):
        rows = self.db.fetchall("SELECT class_id FROM enrollments WHERE student_id = ?", (student_id,))
        return [row[0] for row in rows]
   
    def update_student_enrollment(self, student_id, selected_class_ids):
        current_ids = self. get_enrolled_class_ids(student_id)
        to_add = set(selected_class_ids) - set(current_ids)
        to_remove = set(current_ids) - set(selected_class_ids)

        for class_id in to_add:
            try:
                self.db.execute("INSERT INTO enrollments (student_id, class_id) VALUES (?, ?)", (student_id, class_id))
            except:
                pass

        for class_id in to_remove:
            self.db.execute("DELETE FROM enrollments WHERE student_id = ? AND class_id = ?", (student_id, class_id))
