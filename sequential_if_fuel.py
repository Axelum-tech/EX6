city_A = 0
city_B = 10
city_C = 110
city_D = 150
city_E = 200

volume   =  10   # L
CONSUME  = 2.5/100  # L/KM


print("##########CityB-A###########")

distance_1          = city_B - city_A 
consume_1           = CONSUME * distance_1
if consume_1 <= volume:
    volume    = volume - consume_1
    print("1.The distance till city_B:", distance_1, "KM")
    print("2.The car will consume:", consume_1,"L")
    print("3.Remaining fuel:", volume, "L")
else:
    print("Not enough fuel!")


############################################################
print("##########CityC-B###########")

distance_2          = city_C - city_B 
consume_2           = CONSUME * distance_2

if consume_2 <= volume:
    volume    = volume - consume_2
    print("1.The distance till city_C:", distance_2, "KM")
    print("2.The car will consume:", consume_2,"L")
    print("4.Remaining fuel:", volume, "L")
else:
    print("Not enough fuel!")
###########################################################

print("##########CityD-C###########")

distance_3          = city_D - city_C 
consume_3           = CONSUME * distance_3

if consume_3 <= volume:
    volume    = volume - consume_3
    print("1.The distance till city_D:", distance_3, "KM")
    print("2.The car will consume:", consume_3,"L")
    print("3.Remaining fuel:", volume, "L")
else:
    print("Not enough fuel!")

    ###########################################################

print("##########CityE-D###########")

distance_4          = city_E - city_D 
consume_4           = CONSUME * distance_4

if consume_4 <= volume:
    volume    = volume - consume_4
    print("1.The distance till city_E:", distance_4, "KM")
    print("2.The car will consume:", consume_4,"L")
    print("3.Remaining fuel:", volume, "L")
else:
    print("Not enough fuel!")