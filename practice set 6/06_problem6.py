mark=int(input("Enter the mark:"))

if(90<=mark<=100):
    Grade="Ex"
elif(80<=mark<=89):
    Grade="A"
elif(70<=mark<=79):
    Grade="B"
elif(60<=mark<=69):
    Grade="C"
elif(50<=mark<=59):
    Grade="D"
elif(mark<50):
    Grade="F"

print("your grade is:",Grade)    