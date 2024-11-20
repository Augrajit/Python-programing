try:
    Name = input("Enter the name: ")
    Mark = int(input("Enter the mark: "))
    Phone = int(input("Phone no.: "))
    
    s = "The name of the student is {}, his marks are {} and phone number is {}".format(Name, Mark, Phone)
    print(s)
    
except ValueError:
    print("Please enter valid numeric values for marks and phone number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


