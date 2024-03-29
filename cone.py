import math
class cone:
    def __init__(self, r, h):
        assert r >0 and h>0
        self.r=r
        self.h=h
    def volume(self, r, h):
        l = ((self.r ** 2 + self.h ** 2) ** 0.5)
        return math.pi*self.r*(self.r+l)
    def square(self):
        l=((self.r**2+self.h**2)**0.5)
        kost = round(math.pi, 4)
        return (kost*self.r*(self.r+l))+(kost*self.r**2)
    def __str__(self) -> str:
        return f"cone: r={self.r} h={self.h}"