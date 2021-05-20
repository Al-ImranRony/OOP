

class Fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:                         # When denominator is negative
            self.nr *= -1
            self.dr *= -1
        self._reduce()

    def show(self):
        print(f'{self.nr} / {self.dr}')

    def multiply(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        f = Fraction(self.nr * other.nr, self.dr * other.dr)
        f._reduce()
        return f

    def add(self,other):
        if isinstance(other, int):
            other = Fraction(other)
        f = Fraction(self.nr * other.dr + other.nr * self.dr, self.dr * other.dr)
        f._reduce()
        return f

    @staticmethod
    def hcf(x,y):
        x=abs(x)
        y=abs(y)
        smaller = y if x>y else x
        s = smaller
        while s>0:
            if x%s==0 and y%s==0:
                break
            s-=1
        return s

    def _reduce(self):                          # private instance method _reduce that reduces a fraction to its lowest terms
        h = Fraction.hcf(self.nr, self.dr)
        if h == 0:
            return
        self.nr //= h                           # nominator divided by h, for each  
        self.dr //= h

f1 = Fraction(4,6)
f1.show()
f2 = Fraction(4,-6)
f2.show()
f3 = Fraction(-10,-12)
f3.show()

f4 = f1.multiply(f2)
f4.show()
f5 = f2.add(f3)
f5.show()