def c_to_f():
    return 5*(f-32)/9
f=int(input("The temperature in F is:"))
c=c_to_f()
print(f"{round(c,2)}°C")