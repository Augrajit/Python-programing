# f=open("poem.txt")
# content= f.read()
# if("Twinkle"in content):
#     print("The word twinkle is in the list")
# else:
#     print("The word twinkle is in the list")  
# f.close()    

with open("poem.txt","r") as f:
    content= f.read()
    if("Twinkle" in content):
        print("In list")
    else:
        print("Not in list")
     