#File for making list of members that are entered.


filename = "members.txt"
while True:
    prompt = input("Enter the new name or enter exit to exit: ") + "\n"

    if prompt == "exit" + "\n":
       break

    else:
        file = open(filename, "r")
        members = file.readlines()
        file.close()
        members.append(prompt)
    
        file = open(filename, "w")
        members = file.writelines(members)
        file.close()
    
    
    
print("\nNow the new list of the members is -\n")
file = open(filename, "r")
list = file.readlines()
for i in list:
    print(i)
file.close()