import csv
from HashTable import Hashtable


class Package:

    def __int__(self, package_id, package_address, package_city, package_state, package_zipcode, package_deadline,
                package_kg, package_delivery_status):
        self.package_ID = package_id
        self.package_address = package_address
        self.package_city = package_city
        self.package_state = package_state
        self.package_zipcode = package_zipcode
        self.package_deadline = package_deadline
        self.package_kg = package_kg
        self.package_delivery_status = package_delivery_status
        #self.delivery_time = delivery_time
        #deadline
        #delivery time   <-- add these
        # time departed from hub

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.package_ID, self.package_address,
                                               self.package_city, self.package_state, self.package_zipcode,
                                               self.package_deadline, self.package_delivery_status)#, self.delivery_time)

def package_status(self):



'''
def update(self, status):
    self.status = status

def return_status(self):
        return self.status
'''



# time left hub attribute
