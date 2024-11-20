import random

n=random.randint(1,10)
a=-1
gussess=0
while(a!=n):
    a=int(input("Enter a number between 1-10: "))
    if(a>n):
        print("Lower number please")
    elif(n>a):
        print("Higher number please")
    gussess+=1

print(f"You have gussesed the correct number {n} in {gussess} attempts")        
    