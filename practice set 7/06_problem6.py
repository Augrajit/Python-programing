n=int(input("Enter the number: "))
product=1  #intial product should be 1,not 0
for i in range(1,n+1):
    product=product*i

print(f" The factorial of {n} is :{product}")