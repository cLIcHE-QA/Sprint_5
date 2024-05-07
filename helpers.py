import faker


def get_signup_data():
    fake = faker.Faker()
    name = fake.name()
    email = fake.email()
    password = fake.password()
    return name, email, password
