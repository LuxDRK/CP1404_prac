from silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Hummer", 100, 2)
    taxi.drive(18)
    print(taxi)
    print('Total fare is ${}'.format(taxi.get_fare()))

main()