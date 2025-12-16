# for loop in reverse 
cars = ["Toyota", "Honda", "BMW", "Audi", "Mercedes", "Hyundai", "Kia", "Ford", "Chevrolet", "Nissan",
        "Volkswagen", "Skoda", "Tata", "Mahindra", "Renault", "Jeep", "Volvo", "Fiat", "Peugeot", "Suzuki"]

for item in reversed(cars):
    print(item,end=' ')

print("")
# print 100 to 1 in reverse 
for num in range(100,0,-1):
    print(f"{num:6}",end='')