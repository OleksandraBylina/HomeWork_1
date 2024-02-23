from math import pi


class ball:
    def __init__(self, r):
        assert r > 0
        self.r = r
    def square(self):
        kost=round(pi, 4)
        result = round(4 * kost * self.r ** 2, 4)
        return result

    def volume(self):
        result = (4/3) * pi * self.r ** 3
        return result
    def __str__(self) -> str:
        return f"Ball: r={self.r}"