# Use with Python3 

num = int(input("Enter the monetary value: "))
curr = str(input("Enter the currency type (rupees OR dollars): "))
if curr == "rupees":
    dollars = num * 0.013
    print(num, " rupees is equal to ", dollars, " dollars")
elif curr == "dollars":
    rupees = num * 75.96
    print(num, " dollars is equal to ", rupees, " rupees")
else:
     print("Invalid input")
