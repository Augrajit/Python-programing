'''
* * *
*   *
* * *
'''
n=int(input("Input the number:"))
for i in range(1,n+1):
    if(i==1 or i==n):#As first and third line doesn't have any gap
        print("* "*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")#For the gap
        print("  *",end="")
    print("")    