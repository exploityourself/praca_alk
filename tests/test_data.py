from faker import Faker


class TestData:
    def __init__(self):
        fake = Faker()
        self.username = "asd"
        self.password = "asd"

        self.name = fake.name()
        self.country = fake.country()
        self.city = fake.city()
        self.credit_card = "12334212312312341245"
        self.year = fake.year()
        self.month = fake.month()