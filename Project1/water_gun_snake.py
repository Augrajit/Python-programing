import random
'''
water gun snake game

water=1,gun=-1,snake=0

'''
computer=random.choice([-1,0,1])
youStr=input("Enter your choice: ")
youDict={"s":0,"g":-1,"w":1}
reverseDict={0:"snake",-1:"gun",1:"water"}
you=youDict[youStr]

print(f"You chose:{reverseDict[you]}\nComputer chose:{reverseDict[computer]}")

if(you==computer):
    print("It's a draw")
else:
    if(computer==1 and you==-1):
        print("You Lose!")    
    elif(computer==1 and you==0):
        print("You win!")    
    elif(computer==0 and you==-1):
        print("You win!")    
    elif(computer==0 and you==1):
        print("You Lose!")    
    elif(computer==-1 and you==1):
        print("You win!")    
    elif(computer==-1 and you==0):
        print("You Lose!")    
    else:
        print("Something went wrong")    
       






