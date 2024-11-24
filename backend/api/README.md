# Commands

## Alembic
- Autogenerate migration script based on models: `alembic revision --autogenerate -m "Initial migration"`
- Migrations till latest revision: `alembic upgrade head`
- Downgrade: `alembic downgrade -1`
- Upgrade to a revision: `alembic downgrade -1`
- Blank migration script: `alembic revision -m "description"`