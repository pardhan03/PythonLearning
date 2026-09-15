age = input('Enter the age:')
age_in_int = int(age)

if age_in_int < 13:
    print('Child')
elif age_in_int < 20:
    print('Teenage')
elif age_in_int < 60:
    print('Adult')
else:
    print('Senior')