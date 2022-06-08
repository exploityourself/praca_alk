from faker import Faker


class TestData:
    def __init__(self):
        fake = Faker()
        self.username = "asd"
        self.password = "asd"

        self.name = fake.name()
        self.country = fake.country()
        self.city = fake.city()
        self.credit_card = fake.creditcardnumber()
        self.year = fake.year()
        self.month = fake.month()