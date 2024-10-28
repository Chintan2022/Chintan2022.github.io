#checking probability of head or tail


"""this is the code without data file"""
# head = 0
# tail = 0
# prob = 0
# while True:
#     user_input = input("throw the coin to enter head or tail here: ")
#     match user_input:
#         case "head":
#             head +=1
#             prob = 100 * head/(head+tail)
            
#             print(f"Head: {prob}%")
             
#         case "tail":
#             tail +=1
#             prob = 100 * head/(head+tail)
            
#             print(f"Head: {prob}%")
             
"""this is the code with the data file"""

filename = "sides.txt"
while True:
    with open(filename, "r") as file:
        sides = file.readlines()
    
    
    user_input = input("throw the coin to enter head or tail here: ")+ "\n"
    # print("\n")
    if user_input == "head"+ "\n" or user_input == "tail"+ "\n":
    
        sides.append(user_input)
        
        with open(filename, "w") as file:
            file.writelines(sides)
            
        number_of_heads = sides.count('head\n')
        
        prob = 100 * number_of_heads / len(sides)
        
        print(f"Head: {prob}%")
    
    else:
        print("Sorry, You have entered wrong input")