birth_year  = int(input(" Your birth year"))
CURRENT_YEAR= 2020


age = CURRENT_YEAR - birth_year

if birth_year >= 1900 and birth_year <=2020:
    print("You have:", age, "years")
    
    print("#### Category list ####")
    print('1. 1-3 years - "baby" ' )
    print('2. 4-9 years - "kid"')
    print('3. 10-15 years - "teen"')
    print('4. 16-18 years - "young"')
    print('5. 19-50 years - "adult"')
    print('6. 51+ years - "old"')
    
else : 
    print("Error, insert a correct year format 1990 to 2020")




if birth_year >= 1900 and birth_year <=2020:   

    print("########Your age category###########")
    if age >= 1 and age <= 3:
        print('1. 1-3 years - "baby" ' )
    elif age >= 4 and age <=9:
        print('2. 4-9 years - "kid"')
    elif age >= 10 and age <=15:
        print('3. 10-15 years - "teen"')
    elif age >= 16 and age <=18:
        print('4. 16-18 years - "young"')
    elif age >= 19 and age <=50:
        print('5. 19-50 years - "adult"')
    elif age > 50:
        print('6. 51+ ani - "old"')
 

