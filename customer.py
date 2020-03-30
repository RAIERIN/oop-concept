class Customer:

    def __init__(self):
        """
        Our constructor method which instantiates various customer objects.
        """

        self.cycles = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0
        self.customerName = None
        self.customerPhone = None

    def returnCustPhone(self):
        return self.customerPhone

    def requestCycle(self, customers):
        """
        Takes a request from the customer for the number of cycles.
        """
        custname = input("Please Enter customer Name:")
        if custname.strip() == "":
            print("Customer Name is invalid!")
            return -1
        else:
            self.customerName = custname
        custphone = input("Please Enter Phone Number:")
        try:
            custphone = int(custphone)
        except ValueError:
            print("Phone number should be integer!")
            return -1
        if custphone in customers:
            print("Customer with {} already booked the cycles! You cannot book the cycle!".format(custphone))
            return -1

        cycles = input("How many cycles would you like to rent?")
        try:
            cycles = int(cycles)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if cycles < 1:
            print("Invalid input. Number of cycles should be greater than zero!")
            return -1
        else:
            self.cycles = cycles
            self.customerPhone = custphone
        return self.cycles

    def returnCycle(self, customers):
        """
        Allows customers to return their cycles to the rental shop.
        """
        cust = input("Please Enter Phone Number:")
        try:
            cust = int(cust)
        except ValueError:
            print("Phone number should be integer!")
            return -1
        if cust in customers:
            self.customerPhone = cust
        else:
            print("Customer with {} have not booked the cycle!".format(cust))
            return -1
        print(self.rentalBasis,self.rentalTime,self.cycles)
        if self.rentalBasis and self.rentalTime and self.cycles:
            return self.rentalTime, self.rentalBasis, self.cycles
        else:
            return 0, 0, 0

