class Students:
    def __init__(self, name, batch_no, address):
        self.name = name
        self.batch_no = batch_no
        self.address = address

        def set_age(self,name):
            self.name = Name
        def set_batch_no(self,batch_no):
            self.batch_no = Batch_No
        def set_address(self,address):
            self.address = Address
        def get_name (self,name):
            self.name = name
        def get_batch_no (self, batch_no):
            self.batch_no = batch No
        def get_address (self, address):
            self.address = Address


class DevnationStudents(Students):
    def __init__(self, name, batch_no, address, courses[], marks[]):
        super().__init__(name, batch_no, address)
        self.marks = [];
        self.courses = [];
    def set_courses (self, courses):
        for i in courses:
            if i not in self.courses:
                self.courses.append(i)


    def set_marks(self, courses, marks):
        for i in courses:
            if i not in self.courses:
                self.mark.append(i)


