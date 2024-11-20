n1=int(input("Enter the number of Bangla:"))
n2=int(input("Enter the number of English:"))
n3=int(input("Enter the number of Math:"))

if((n1+n2+n3)/3>=40 and n1>33 and n2>33 and n3>33):
    print("You are pass")
else:
    print("FAIL")