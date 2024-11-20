class vector:
    def __init__(self,l) :
       self.l=l
    def __len__(self):
        return len(self.l)  

v1=vector([3,4,8])
           

print(len(v1))
