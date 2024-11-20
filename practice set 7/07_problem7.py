'''
  *    (2 gaps)
 ***   (1 gap)
*****  (0 gap)

'''
n=int(input("Input the number:"))

for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("")    