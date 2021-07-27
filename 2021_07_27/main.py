class myType:
    def __new__(cls,a,b):
        if a<500:
            inst= object.__new__(cls)
            return inst


    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        x = self.a + other.a
        y = self.b + other.b
        return (x,y)
    def __sub__(self, other):
        x = self.a - other.a
        y = self.b - other.b
        return (x,y)

    def __gt__(self, other):
        if self.a + self.b > other.a + other.b
            return True
        else:
            return False
    def __it__(self, other):
        if self.a + self.b < other.a + other.b
            return True
        else:
            return False
