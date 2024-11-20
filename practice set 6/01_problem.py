n1=int(input("Enter the number: "))
n2=int(input("Enter the number: "))
n3=int(input("Enter the number: "))
n4=int(input("Enter the number: "))

if(n1>n2 and n1>n3 and n1>n4):
  print("The greatest number is:",n1)

elif(n2>n1 and n2>n3 and n2>n4):
  print("The greatest number is:",n2)

elif(n3>n2 and n3>n4 and n3>n4):
  print("The greatest number is:",n3)

elif(n4>n2 and n4>n3 and n4>n1):
  print("The greatest number is:",n4)