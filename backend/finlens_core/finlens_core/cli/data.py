import random
import string
from datetime import timedelta
from typing import Generator

from faker import Faker
from faker.providers import BaseProvider
from src.models import Bank, User

fake = Faker("en_US")


class UserFakeDataProvider(BaseProvider):
    def permanent_account_number(self):
        """Generate PAN number in format XXXXX9999X"""
        seq = random.choices(string.ascii_uppercase, k=5)
        seq.extend(random.choices(string.digits, k=4))
        seq.append(random.choice(string.ascii_uppercase))
        return "".join(seq)


fake.add_provider(UserFakeDataProvider)


def get_fake_user_data() -> dict[str, str]:
    return {
        "pan": fake.permanent_account_number(),
        "name": fake.name(),
        "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=115),
        "email": fake.email(),
        "address": fake.address(),
        "latitude": fake.latitude(),
        "longitude": fake.longitude(),
    }


def get_fake_bank_data() -> list[dict[str, str]]:
    """A manually generated bank data set"""
    return [
        {
            "name": "HDFC Bank",
            "email": "helpdesk@hdfcbank.com",
            "code": "HDFC",
        },
        {
            "name": "ICICI Bank",
            "email": "servicedesk@icicibank.com",
            "code": "ICICI",
        },
        {
            "name": "Yes Bank",
            "email": "helpdesk@yesbank.com",
            "code": "YES",
        },
        {
            "name": "State Bank of India",
            "email": "customercare@sbi.com",
            "code": "SBI",
        },
        {
            "name": "Axis Bank",
            "email": "help@axisbank.com",
            "code": "AXIS",
        },
        {
            "name": "Bank of Baroda",
            "email": "servicedesk@bankofbaroda.com",
            "code": "BOB",
        },
        {
            "name": "Union Bank of India",
            "email": "customercare@unionbank.co.in",
            "code": "UBI",
        },
    ]


def get_fake_bank_accounts(
    users: list[User], banks: list[Bank]
) -> Generator[dict[str, str], None, None]:
    """Generate fake bank account data based on supplied user and bank records"""
    banks_ln = len(banks)
    for user in users:
        bank_subset = random.choices(banks, k=random.randint(1, banks_ln))
        for bank in bank_subset:
            yield {
                "number": fake.iban(),
                "date_of_opening": fake.date_between(
                    start_date=user.date_of_birth + timedelta(365 * 18),
                    end_date=user.date_of_birth + timedelta(365 * 60),
                ),
                "bank": bank,
                "user": user,
            }
