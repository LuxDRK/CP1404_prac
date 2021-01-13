from car import Car
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    total_fare = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!\nq)uit, c)hoose taxi, d)rive")
    menu= input(">>> ").lower()
    while menu != 'q':
        if menu == 'c':
            print('Taxis available:')
            for i, taxi in enumerate(taxis):
                print("{} - {}".format(i, taxi))
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
        elif menu == 'd':
            current_taxi.start_fare()
            distance_to_drive = float(input("Drive how far? "))
            current_taxi.drive(distance_to_drive)
            trip_cost = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name,trip_cost))
            total_fare = total_fare + trip_cost
        else:
            print('Invalid option')
        print("Bill to date: ${:.2f}".format(total_fare))
        print('q)uit, c)hoose taxi, d)rive')
        menu = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    display_taxis(taxis)


main()