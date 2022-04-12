class Animal():

    def __init__(self, id, name, breed, status, location_id, customer_id, location = None, customer = None):
        self.id = id
        self.name = name
        self.breed = breed
        self.status = status
        self.location_id = location_id
        self.customer_id = customer_id
        self.location = location
        self.customer = customer