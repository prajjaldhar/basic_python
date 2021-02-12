class C2dVec:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"
class C3dVec(C2dVec):
    def __init__(self,i,j,k):
        super().__init__(i,j)#base class constructor is displaying
        self.kcap=k
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
if __name__ == "__main__":
    v2d=C2dVec(1,3)
    v3d=C3dVec(5,8,4)
    print(v2d)
    print(v3d)