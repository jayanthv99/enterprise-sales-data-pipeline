from faker import Faker
import pandas as pd
import random
from pathlib import Path

from python.utils.constants import (
    LOYALTY_TIERS,
    GENDERS,
    ACTIVE_STATUS,
    COUNTRY,
    NUM_CUSTOMERS,
)

fake = Faker("en_IN")

def generate_customer(customer_id):
    return {
        "customer_id": f"C{customer_id:06d}",
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "gender": fake.random_element(elements=GENDERS),
        "email": fake.email(),
        "phone": fake.msisdn()[:10],
        "city": fake.city(),
        "state": fake.state(),
        "country": COUNTRY,
        "registration_date": fake.date_between(start_date="-5y", end_date="today"),
        "loyalty_tier": fake.random_element(elements=LOYALTY_TIERS),
        "is_active": fake.random_element(elements=ACTIVE_STATUS)
    }

customers = []

for i in range(1, NUM_CUSTOMERS + 1):
    customers.append(generate_customer(i))

df = pd.DataFrame(customers)

BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = BASE_DIR / "data" / "raw"

RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

df.to_csv(
    RAW_DATA_DIR / "customers.csv",
    index=False
)

assert len(df) == NUM_CUSTOMERS
assert df["customer_id"].is_unique

print(f"Successfully generated {len(df)} customer records.")

