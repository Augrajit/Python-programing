class Demo:
    a=5
o=Demo()
print(o.a)#prints class attribure when object attribute is
          #not present
o.a=0 #input a object attribute
print(o.a)#prints object attribure when object attribure 
          #is present
print(Demo.a )
