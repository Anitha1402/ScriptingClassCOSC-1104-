# Age classification application
# Classify ages as: baby, toddler, teenager, adult, middle age, senior

# Ages to consider: 6, 15, 20, 40, 45, 65, 75, 97
age = int(input('Please Enter Age: '))

if (age >= 90):
    print('Almost Dead')
elif (age >= 70):
    print('Senior')
elif (age >= 40):
    print('Middle Age')
elif (age >= 20):
    print('Adult')
elif (age >= 13):
    print('Teenager')
elif (age >= 3):
    print('Toddler')
else:
    print('Baby')