class Student:
    def __init__(self, first, last, gpa):
        self.first = first
        self.last = last
        self.gpa = gpa

    def get_gpa(self):
        return self.gpa