class Patient:
    def __init__(self, full_name, date_of_birth, gender, address, phone, email):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.address = address
        self.phone = phone
        self.email = email

    def to_dict(self):
        return self.__dict__
