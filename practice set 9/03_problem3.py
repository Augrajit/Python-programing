def generate_table(n):
    table=""
    for i in range(1,11):
        table+=f"{n}X{i}={n*i}\n"
    with open (f"Tables/table_{n}.txt","w") as f:
                 #syntex:folder/file
        f.write(table)


for i in range(2,21):
    generate_table(i)