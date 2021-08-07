class student:
    def __init__(self, name, batch_no, address, age, father_name, city):
        self.name = name
        self.batch_no = batch_no
        self.address= address
        self.age = age
        self.father_name= father_name
        self.city = city

    def __new__(cls,age,location):
        if age <= 18 and (location=='Karachi' or location=='Lahore' or location == 'Islamabad' or location== 'Faisalabad'):
            inst= object.__new__(cls)
            return inst


    def set_age(self, name):
        self.name = name

    def set_batch_no(self, batch_no):
        self.batch_no = batch_no

    def set_address(self, address):
        self.address = address

    def set_address(self, father_name):
        self.address = father_name

    def set_address(self, city):
        self.address = city


    def get_name(self, name):
        self.name = name

    def get_batch_no(self, batch_no):
        self.batch_no = batch_no

    def get_address(self, address):
        self.address = address

    def get_address(self, father_name):
        self.address = father_name

    def get_address(self, city):
        self.address = city


class devnationStudents(student):

    def __init__(self, name, batch_no, address, age, father_name, city, courses=[], marks=[]):
        super().__init__(name, batch_no, address, age, father_name, city)
        self.courses = courses
        self.marks = marks
        self.courses_score = []

    def add_courses(self, courses):

        for i in courses:
            if i not in self.courses:
                self.courses.append(i)

    def add_courses_score(self, courses, courses_score):

        if courses in self.courses:

            if courses not in self.courses_score:
                self.courses_score.append({'course': courses, 'marks': courses_score})

        else:
            return

    def get_courses(self):
        self.courses

    def get_marks(self):
        self.courses_score


