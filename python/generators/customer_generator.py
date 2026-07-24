from faker import Faker
import pandas as pd
import random
from pathlib import Path

fake = Faker("en_IN")

NUM_CUSTOMERS = 1000

def generate_customer(customer_id):
    return {
        "customer_id": f"C{customer_id:06d}",
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "gender": random.choice(["Male", "Female"]),
        "email": fake.email(),
        "phone": fake.msisdn()[:10],
        "city": fake.city(),
        "state": fake.state(),
        "country": "India",
        "registration_date": fake.date_between(start_date="-5y", end_date="today"),
        "loyalty_tier": random.choice(["Silver", "Gold", "Platinum"]),
        "is_active": random.choice(["Yes", "No"])
    }

customer = generate_customer(1)
print(customer)