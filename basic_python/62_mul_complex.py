class Complex:
    def __init__(self,r,img):
        self.real=r
        self.imaginary=img
    def __add__(self,c):
        return Complex(self.real+c.real,self.imaginary+c.imaginary)
    def __mul__(self,c):
        mulReal=self.real*c.real-self.imaginary*c.imaginary
        mulImg=self.real*c.imaginary-self.imaginary*c.real
        return Complex(mulReal,mulImg)
    def __str__(self):
        if self.imaginary<0:
            return f"{self.real} - {-self.imaginary}j"
        else:
            return f"{self.real} + {self.imaginary}j"
c1=Complex(1,-4)
c2=Complex(1,-8)
add=c1+c2
print(c1)
print(c2)
print(add)
mul=c1*c2
print(mul)