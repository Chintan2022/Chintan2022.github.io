"""this is currency converter used to convert indian rupees to any other currency that is given base on the text file"""

with open("Currency.txt") as f:
    lines = f.readlines()
# print(lines)

currency_dict = {}
for line in lines:
    parsed_data = (line.split("\t"))
    currency_dict[parsed_data[0]] = parsed_data[1]
    
    
# print(currency_dict)
amount = float(input("Please Enter the amount : \n"))
print("Enter the name of the currency you want to convert to, these are the available options : \n")

[print(item) for item in currency_dict.keys()]

currency = input("Please Enter the currency name : \n")

print(f"{amount} INR is equal to {amount * float(currency_dict[currency])} {currency}")

