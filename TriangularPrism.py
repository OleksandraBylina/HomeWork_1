class triangularprism:
    def __init__(self, a, b, c, l):
        assert a+b>c and b+c>a and c+a>b and a>0 and b>0 and c>0 and l>0
        self.a = a
        self.b = b
        self.c = c
        self.l = l

    def semiperimeter(self):
        return self.perimeter_bone() / 2
    def perimeter_bone(self):
        return self.a + self.b + self.c

    def square(self):
        result_tr = ((self.semiperimeter() * (self.semiperimeter() - self.a) * (self.semiperimeter() - self.b) * (self.semiperimeter() - self.c)) ** 0.5)
        result_re = (self.a * self.l + self.b * self.l + self.c * self.l)
        result = (result_tr * 2 + result_re)
        result = round(result.real, 2) + round(result.imag, 2) * 1j
        result_list = [round(result.real, 2), round(result.imag, 2)]
        ressy=max(result_list)
        return ressy

    def volume(self):
        result_tr = (self.semiperimeter() * (self.semiperimeter() - self.a) * (self.semiperimeter() - self.b) * (self.semiperimeter() - self.c)) ** 0.5
        return result_tr * self.l

    def __str__(self) -> str:
        return f"TriangularPrism: a={self.a} b={self.b} c={self.c} l={self.l}"