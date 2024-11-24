from typing import Annotated

import typer
from faker import Faker
from rich.progress import track
from sqlalchemy import delete
from sqlalchemy.exc import IntegrityError
from src.cli.data import get_fake_bank_accounts, get_fake_bank_data, get_fake_user_data
from src.dependencies import get_db_session
from src.models import Bank, BankAccount, User

app = typer.Typer()
fake = Faker("en_US")


@app.command()
def load_data(
    user_records: Annotated[
        int, typer.Argument(help="Number of users to be generated")
    ] = 1000,
):
    """Load mock data in db"""
    with get_db_session() as session:
        # creating banks
        bank_records = get_fake_bank_data()
        bank_records_ln = len(bank_records)
        for value in track(range(bank_records_ln), description="Creating Banks..."):
            bank = Bank(**bank_records[value])
            session.add(bank)
            session.commit()
        print(f"{bank_records_ln} banks created")

        # creating users
        for value in track(range(user_records), description="Creating Users..."):
            user_data = get_fake_user_data()
            user = User(**user_data)
            session.add(user)
            try:
                session.commit()
            except IntegrityError:
                # suppress integrity error at time of mock data creation
                session.rollback()
        print(f"{user_records} users created")

        # creating bank accounts
        users = session.query(User).all()
        banks = session.query(Bank).all()
        bank_account_nos = 0
        print(f"Found {len(users)} users and {len(banks)} banks")
        for bank_account_data in track(
            get_fake_bank_accounts(users, banks),
            description="Creating Bank Accounts...",
        ):
            bank_account = BankAccount(**bank_account_data)
            session.add(bank_account)
            try:
                session.commit()
            except IntegrityError:
                # suppress integrity error at time of mock data creation
                session.rollback()
            bank_account_nos += 1
        print(f"{bank_account_nos} bank accounts created")

    print("Execution complete")


MODELS = [
    # maintain order of deletion
    ("BankAccount", BankAccount),  # 3
    ("User", User),  # 2
    ("Bank", Bank),  # 1
]


@app.command()
def clear_data():
    """Delete data from all tables. Keep the schema."""
    for name, model in track(MODELS, description="Deleting..."):
        with get_db_session() as session:
            session.execute(delete(model))
            print(name)
    print("Execution complete")


@app.command()
def data_status():
    """Check current status of mock data in db"""
    with get_db_session() as session:
        for name, model in MODELS:
            count = session.query(model).count()
            print(f"{name}: {count}")
    print("Execution complete")


if __name__ == "__main__":
    app()
