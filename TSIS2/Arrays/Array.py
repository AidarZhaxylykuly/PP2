cars = ["Ford", "Volvo", "BMW"]
print(cars)
#['Ford', 'Volvo', 'BMW']


x = cars[0]
print(x)
#Ford


cars[0]="Toyota"
print(cars)
#["Toyota", "Volvo", "BMW"]


x = len(cars)
print(x)
#3


cars = ["Ford", "Volvo", "BMW"]
for x in cars:
    print(x)
'''
Ford
Volvo
BMW
'''


cars.append("Honda")
print(cars)
'''
Ford
Volvo
BMW
Honda
'''


cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
print(cars)
'''
Ford
BMW
'''


cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print(cars)
'''
Ford
BMW
'''