class vector:
    def __init__(self,i,j,k) :
        self.i=i
        self.j=j
        self.k=k

    def __add__ (self,v2):
        return vector(self.i+v2.i,self.j+v2.j,self.k+v2.k) 
    def __mul__(self,v2):
        return (self.i*v2.i+ self.j*v2.j+ self.k*v2.k)

    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"

v1=vector(3,4,8)
v2=vector(2,9,7)           

print(v1+v2)
print(v1*v2)