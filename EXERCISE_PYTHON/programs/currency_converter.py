with open('convert_currency.txt')as f:
    datas=f.readlines()
currency_dict={}
for data in datas:
    observation=data.split("\t")
    currency_dict[observation[0]]=observation[1]
data_convert=int(input("ENTER AMOUNT: \n"))
print("ENTER THE NAME OF CURRENCY YOU WANT TO CONVERT THIS AMOUNT TO? AVALIBLE OPTIONS ARE:\n")
#list comprehensions
[print(item) for item in currency_dict.keys()]
currency=input("ENTER ONE OF THE ABOVE VALUES:\n")
print(f"{data_convert} INR IS EQUALS TO {data_convert*float(currency_dict[currency])} THIS MUCH {currency.upper()} ")

