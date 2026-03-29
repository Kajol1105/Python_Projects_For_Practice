rent = int(input("Enter your flat rent ="))
food = int(input("Enter the amount of food ordered = "))
electricity= int(input("Enter the toral of electricity bill = "))
charge_unit = int(input("Enter the charge per unit= "))
no_of_people= int(input("Enter the number of room mates"))


total_bill = electricity * charge_unit

output =  (rent +food +total_bill)//no_of_people
print("Each person will pay = " , output)

""" / vs // in python
/ is the division operator that returns a float result, while // is the floor division operator that returns an integer result by rounding down to the nearest whole number. For example:
5 / 2  # returns 2.5
5 // 2  # returns 2
"""
