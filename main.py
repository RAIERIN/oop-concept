from cycleRental import CycleRental
from customer import Customer


def main():
    shop = CycleRental(100)
    customer = Customer()
    customers = []
    while True:
        print("""
        ====== Bike Rental Shop =======
        1. Display available bikes
        2. Request a bike on hourly basis $5
        3. Request a bike on daily basis $20
        4. Request a bike on weekly basis $60
        5. Return a bike`
        6. Display Customer Number List
        7. Exit
        """)

        choice = input("Enter choice: ")

        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            continue

        if choice == 1:
            shop.displaystock()

        elif choice == 2:
            res = customer.requestCycle(customers)
            if res != -1:
                customer.rentalTime = shop.rentCycleOnHourlyBasis(res, customer.customerName, customer.customerPhone)
                customer.rentalBasis = 1
                customers.append(customer.customerPhone)
            else:
                continue
        elif choice == 3:
            res = customer.requestCycle(customers)
            if res != -1:
                customer.rentalTime = shop.rentCycleOnDailyBasis(res, customer.customerName, customer.customerPhone)
                customer.rentalBasis = 2
                customers.append(customer.customerPhone)
            else:
                continue
        elif choice == 4:
            res = customer.requestCycle(customers)
            if res!=-1:
                customer.rentalTime = shop.rentCycleOnWeeklyBasis(res, customer.customerName, customer.customerPhone)
                customer.rentalBasis = 3
                customers.append(customer.customerPhone)
            else:
                continue
        elif choice == 5:
            res = customer.returnCycle(customers)
            if res != -1:
                customer.bill = shop.returnCycle(res)
                customers.remove(customer.customerPhone)
                customer.rentalBasis, customer.rentalTime, customer.bikes = 0, 0, 0
            else:
                continue
        elif choice == 6:
            print(customers)
        elif choice == 7:
            break
        else:
            print("Invalid input. Please enter number between 1-6 ")
    print("Thank you for using the bike rental system.")


if __name__ == "__main__":
    main()