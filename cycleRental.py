import datetime

class CycleRental:
    def __init__(self, stock=0):
        """
        Our constructor class that instantiates cycle rental shop
        """
        self.stock = stock

    def displaystock(self):
        """Displays the Cycles currently available for rent in the shop"""
        print("We currently have {} Cycles available for rent.".format(self.stock))
        return  self.stock

    def rentCycleOnHourlyBasis(self, n, name, phone):
        """
        :param n:
        :return: message accordingly
        Rents a cycle on hourly basis to a customer
        """
        if n <= 0:
            print("Cycle is out of stock!")
            return None
        elif n > self.stock:
            print("Sorry! We have currently {} cycles available to rent.".format(self.stock))
            return None
        else:
            now = datetime.datetime.now()
            print("{} with phone number {} have rented a {} cycle(s) on hourly basis today at {} hours.".format(name, phone, n, now.hour))
            print("You will be charged $5 for each hour per cycle.")
            print("We hope that you enjoy our service.")

            self.stock -= n
            return  now

    def rentCycleOnDailyBasis(self, n, name, phone):
        """
        Rents a cycle on daily basis to a customer.
        :param n:
        :return: message accordingly
        """
        if n <= 0:
            print("Cycle is out of Stock!")
            return None

        elif n > self.stock:
            print("Sorry! We have currently {} cycle(s) available to rent.".format(self.stock))
            return None

        else:
            now = datetime.datetime.now()
            print("{} with phone number {} have rented a {} cycle(s) on daily basis today at {} hours.".format(name,phone,n,now.hour))

            print("You will be charged $20 for each day per cycle.")
            print("We hope that you enjoy our service.")

            self.stock -= n
            return now

    def rentCycleOnWeeklyBasis(self, n, name, phone):
        """
        Rents a cycle on weekly basis to a customer.
        """
        if n <= 0:
            print("Cycle out of stock!")
            return None

        elif n > self.stock:
            print("Sorry! We have currently {} cycle(s) available to rent.".format(self.stock))
            return None

        else:
            now = datetime.datetime.now()
            print("{} with phone number {} have rented a {} cycle(s) on weekly basis today at {} hours.".format(name,phone, n,  now.hour))
            print("You will be charged $60 for each week per cycle.")
            print("We hope that you enjoy our service.")
            self.stock -= n

            return now

    def returnCycle(self, customers):
        """
        1. Accept a rented cycle from a customer
        2. Replensihes the inventory
        3. Return a bill
        """

        phone = input("Please Enter Phone Number:")
        try:
            phone = int(phone)
        except ValueError:
            print("Phone number should be integer!")
            return -1

        data = next((item for item in customers if item["phone"] == phone), False)

        if data == False:
            print("Customer with {} have not booked the cycle!".format(phone))
            return -1
        custs = list(filter(lambda i: i['phone'] != phone, customers))
        bill = 0

        if data['rentalTime'] and data["rentalBasis"] and data['cycles']:
            self.stock += data['cycles']
            now = datetime.datetime.now()
            rentalPeriod = now - data['rentalTime']

            # hourly bill calculation
            if data["rentalBasis"] == 1:
                bill = round(rentalPeriod.seconds / 3600) * 5 * data['cycles']

            # daily bill calculation
            elif data["rentalBasis"] == 2:
                bill = round(rentalPeriod.days) * 20 * data['cycles']

            # weekly bill calculation
            elif data["rentalBasis"] == 3:
                bill = round(rentalPeriod.days / 7) * 60 * data['cycles']

            if (3 <= data['cycles'] <= 5):
                print("You are eligible for Family rental promotion of 30% discount")
                bill = bill * 0.7

            print("Thanks for returning your bike. Hope you enjoyed our service!")
            print("That would be ${}".format(bill))
            data['bill'] = bill
            res = {"billDetail": data, "customers": custs}
            return res
        else:
            print("Are you sure you rented a cycle with us?")
            return None
