def divisable5(n):
    if(n%5 ==0):
        return True
    else:
        return False
    
a=[8734,5,55,90]

f=list(filter(divisable5,a))
print(f)