# Book your ride

print("Select your ride")
print("1. Bike")
print("2.Car")

choice = int(input("Enter your choice, type '1' or '2' :"))
if choice == 1:
    print("What type of BIKE ? ")
    print("1.Scooty")
    print("2. Scooter")

    bike_choice = int(input("Enter yor choice of bike, type '1' or '2' : "))
    if bike_choice ==1:
        print("Your ride with Scooty is confirmed")
    else:
        print("Your ride with Scooter is confirmed")
    
elif choice == 2:
    print("What type of CAR ? ")
    print("1.SEDAN")
    print("1.SUV")
    car_choice = int(input("Enter your choice,type '1' or '2' : "))
    if car_choice == 1:
        print("You have selected SEDAN")
    else:
        print("You have selected SUV")

else:
    print("Wrong input")

                     