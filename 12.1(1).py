class TRectangle():
    def __init__(self, a = 1, b = 1):
        self.a = a
        self.b = b
        self.a_print()
        self.b_print()
    @property
    def a(self):
        return self.__a
    @a.setter
    def a(self, value):
        if value > 0:
            self.__a = value
        else:
            raise Exception('nedopustymo!')

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if value > 0:
            self.__b = value
        else:
            raise Exception('nedopustymo!')
    def a_print(self):
        self.a = float(input('vvedit a '))
        print('a = ', self.a)
    def b_print(self):
        self.b = float(input('vvedit b '))
        print('b = ', self.b)
    def area(self):
        return  self.a*self.b
    def perimetr(self):
        return 2*self.a+2*self.b
    def __add__(self, other_side):
        return TRectangle(self.a+other_side.a, self.b+other_side.b)
    def __sub__(self, other_side):
        return TRectangle(self.a-other_side.a, self.b-other_side.b)
    def __mul__(self, other_side):
        return TRectangle(self.a*other_side.a, self.b*other_side.b)

rect1 = TRectangle(3,4)
print(rect1.area())
print(rect1.perimetr())

rect2 = TRectangle(2, 4)
print(rect2.area())
print(rect2.perimetr())