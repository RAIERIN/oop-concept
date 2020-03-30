from cycleRental import CycleRental
from customer import Customer


def main():
    shop = CycleRental(100)
    customer = Customer()
    customers = []
    oldCustomer=[]
    while True:
        print("""
        ====== Bike Rental Shop =======
        1. Display available bikes
        2. Request a bike on hourly basis $5
        3. Request a bike on daily basis $20
        4. Request a bike on weekly basis $60
        5. Return a bike`
        6. Display Customer List
        7. Display Old Customer List
        8. Exit
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
                detail = {"cycles": customer.cycles, "phone": customer.customerPhone, "rentalTime": customer.rentalTime, "rentalBasis": customer.rentalBasis, "name": customer.customerName}
                customers.append(detail)
            else:
                continue
        elif choice == 3:
            res = customer.requestCycle(customers)
            if res != -1:
                customer.rentalTime = shop.rentCycleOnDailyBasis(res, customer.customerName, customer.customerPhone)
                customer.rentalBasis = 2
                detail = {"cycles": customer.cycles, "phone": customer.customerPhone, "rentalTime": customer.rentalTime,
                          "rentalBasis": customer.rentalBasis, "name": customer.customerName}
                customers.append(detail)
            else:
                continue
        elif choice == 4:
            res = customer.requestCycle(customers)
            if res != -1:
                customer.rentalTime = shop.rentCycleOnWeeklyBasis(res, customer.customerName, customer.customerPhone)
                customer.rentalBasis = 3
                detail = {"cycles": customer.cycles, "phone": customer.customerPhone, "rentalTime": customer.rentalTime,
                          "rentalBasis": customer.rentalBasis, "name": customer.customerName}
                customers.append(detail)
            else:
                continue
        elif choice == 5:
            res = shop.returnCycle(customers)
            if res != -1:
                customers = res['customers']
                oldCustomer.append(res['billDetail'])
        elif choice == 6:
            print(customers)
        elif choice == 7:
            print(oldCustomer)
        elif choice == 8:
            break
        else:
            print("Invalid input. Please enter number between 1-6 ")
    print("Thank you for using the bike rental system.")


if __name__ == "__main__":
    main()