from faker import Faker


class TestData:
    def __init__(self):
        fake = Faker()
        self.fake_username = fake.email()
        self.fake_password = fake.password()
        self.real_username = "asd"
        self.real_password = "asd"

        self.name = fake.name()
        self.country = fake.country()
        self.city = fake.city()
        self.credit_card = fake.creditcardnumber()
        self.year = fake.year()
        self.month = fake.month()