c1="Make a lot of money"
c2="buy now"
c3="subscribe this"
c4="click this"

Comment=input("Enter a comment ")

if(c1 in Comment or c2 in Comment or c3 in Comment or 
   c4 in Comment):#uses of in
    print("Spam detected")
else:
    print("This comment is not a spam")