# n=int(input("Enter the number: "))
# for i in range(1,11):
#     print(f"{n}x{i}={i*n}")


# n=int(input("Enter the number: "))
# i=1
# while (i<11):
#     print(f"{n}x{i}={i*n}")
#     i+=1

# n=5
# product=1
# for i in range (1,n+1):
#     product=product*i
# print(f"The factorial is:{product}")    


# n=3
# for i in range(1,4):
#     print(" "*(n-i),end="")
#     print("*"*(2*i -1),end="")
#     print("")


# n=3
# for i in range (1,4):
#     print("*"*(i))
   

n=5
def factorial(i):
    if(i==0 or i==1):
        return 1
    else:
        return n*factorial(n-1)



