from functools import reduce

def greater(a,b):
    if(a>b):
        return a
    else:
        return b
    
l=[23,423,5,3,23,245,245,135,55]

print(reduce(greater,l))