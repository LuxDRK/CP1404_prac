from taxi import Taxi

def main():
    taxi_info = Taxi('Prius', 100)
    taxi_info.drive(40)
    print('{}\nTotal fare is ${}'.format(taxi_info,taxi_info.get_fare()))
    taxi_info.start_fare()
    taxi_info.drive(100)
    print('{}\nTotal fare is ${}'.format(taxi_info,taxi_info.get_fare()))


main()