from datetime import datetime
import random
from Customer import Customer

class Car:
    CARS_AVAILABLE = 10
    HOURLY_RENT = 3
    DAILY_RENT = 50
    WEEKLY_RENT = 300
    BOOKINGS = dict()
    
    def __init__(self, customer: Customer):
        self.bookingTime = datetime.now()
        if not isinstance(customer, Customer):
            print(f'Parameter {customer} is not of type Customer\nPlease initialize Car object with correct paremeter')
        self.__customer = customer

    def displayAvailableCars(self):
        print(f'We have {Car.CARS_AVAILABLE} cars available right now!')
        print(self.bookingTime, type(self.bookingTime))
        print(self.__customer, type(self.__customer))

    def rentHourlyCar(self, carsRequested):
        if validateRequestedCars(self, carsRequested):
            Car.BOOKINGS[self.__customer.phone] = [carsRequested]
            Car.CARS_AVAILABLE -= carsRequested
            print(f'You have booked {carsRequested} cars on hour basis at ${HOURLY_RENT}/Hour')

    def rentDailyCar(self, carsRequested):
        if validateRequestedCars(self, carsRequested):
            Car.BOOKINGS[self.__customer.phone] = [carsRequested]
            Car.CARS_AVAILABLE -= carsRequested
            print(f'You have booked {carsRequested} cars on daily basis at ${DAILY_RENT}/Day')

    def rentWeeklyCar(self, carsRequested):
        if validateRequestedCars(self, carsRequested):
            Car.BOOKINGS[self.__customer.phone] = [carsRequested]
            Car.CARS_AVAILABLE -= carsRequested
            print(f'You have booked {carsRequested} cars on weekly basis at ${WEEKLY_RENT}/Week')

    def validateRequestedCars(self, carsRequested):
        if carsRequested <= 0:
            print('Invalid input')
            return False
        elif carsRequested > Car.CARS_AVAILABLE:
            print('Requested cars exceeded the available car count')
            self.displayAvailableCars()
            return False
        return True

