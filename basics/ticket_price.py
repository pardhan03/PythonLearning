age = input("Input the age of the user:")
day = input("Enter the day:")
price = 12 if int(age) >= 18 else 8

if day == 'Monday':
    price = price -2

print(price)