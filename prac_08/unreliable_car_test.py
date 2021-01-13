from unreliable_car import UnreliableCar

def main():

    car = UnreliableCar('Prius', 100, 50)

    for i in range(1, 20):
        print('Attempting to drive {}km:'''.format(i))
        print("{} drive {:2}km".format(car.name, car.drive(i)))

    print(car)

main()