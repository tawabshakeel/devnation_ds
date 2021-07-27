class myType():
    def __new__(cls, a, b):
        if a < 500:
            ad = object.__new__(cls)
            return ad
           # ?exit()
        # else:
        #     ad = object.__new__(cls)
        #     return ad

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a + other.a, self.b + other.b
    def __sub__(self, other):
        return self.a - other.a, self.b - other.b
    def __gt__(self, other):
        return self.a > other.a, self.b > other.b
    def __lt__(self, other):
        return self.a < other.a, self.b < other.b



t1 = myType(1, 2)
t2 = myType(2, 3)
print(t1 + t2)
print(t1 - t2)
print(t1 > t2)
print(t1 < t2)
