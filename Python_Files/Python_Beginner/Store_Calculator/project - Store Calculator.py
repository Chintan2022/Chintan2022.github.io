vegetable_list = [
    ["Tomato", "Potato", "Lemon", "Cucumber", "Coriander", "Onion", "Carrot", "Broccoli", "Spinach", "Capsicum", "Cauliflower", "Eggplant"],
    [20, 10, 20, 15, 12, 8, 18, 25, 22, 30, 28, 35]]

print("*** Hello in the Chintan's Veggies store, here is the list of the items ***")

for i in range(len(vegetable_list[0])):
    print(f"{i+1} . {vegetable_list[0][i]} - {vegetable_list[1][i]}")
    
print("You have to select the number of the items to select that item... \n")
sum = 0
groceries = []

i=0

#This while loop will be used for takin orders until q is entered to quit...
while(True):
    number = input("Enter the item number or press q to quit:")
    # kg = int(input("Enter the KG number or press q to quit: \n"))
    
    if(number != "q"):
        
        kg = int(input("Enter the KG in number or press q to quit:"))
        
        sum  = sum + (vegetable_list[1][int(number)-1]) * kg
        i+=1
        
        groceries.append(f"{i} - {vegetable_list[0][int(number)-1]} with {kg} kgs - {(vegetable_list[1][int(number)-1]) * kg} rs")
        
        print(f"\nYou chose {vegetable_list[0][int(number)-1]} with amount of {kg} kgs")
        print(f"Your order total so far: {sum} \n")
    
    else:
        print("\nThanks for using the Store Calcultor\n")
        print("This is the receipt of your total purchase\n")
        for grocery in groceries:
            print(grocery)
        print(f"\n---------- Your total bill is {sum} --------\n")
        break