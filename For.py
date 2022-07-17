cars = ["Bmw", "Honda", "Fiat", "Volvo"]

for car in range(len(cars)):
    if car == 0:
        print(cars[car] + " is the Best Car Ever ☺")
    else:
        print("But " + cars[car] + " is also good")