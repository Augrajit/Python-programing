'''
sum(1)=1
sum(2)=1+2
sum(3)=1+2+3

sum(n)=1+2+3+4+..........+n
      =sum(n-1)+n
'''
n=int(input("Enter the value of n: "))
def sum(n):
    if(n==1):
        return 1
    else:
        return sum(n-1)+n
print(sum(n))