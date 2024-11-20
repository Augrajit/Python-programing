word="python"
with open("log.txt") as f:
    content=f.read()
if(word in content):
    print("Yes it is")
else:
    print("No python")