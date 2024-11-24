# finlens
FinLens - Seamless Transactions, Sharp Insights.
A highly performant system architecture that can handle high volume of transactions and generate real time insights.

## System Design and Architecture

### Entities, Relationships and Database Schema
1. Bank
   1. Schema: `id: uuid`, `name: string`, `code: string`, `email: string`, `phone: string` 
   2. Relationships: Isolated, strong entity.
2. Customer
   1. Schema: `id: uuid`, `name: string`, `pan: string`, `email: string`, `phone: string`, `address: string`, `latitude: float`, `longitude: float`
   2. Relationships: Isolated, strong entity
3. Bank Account
   1. Schema: `id: uuid`, `bank_id: uuid`, `customer_id: uuid`
   2. Relationships: Weak entity
      1. A customer can have at most one account with a bank.
      2. A bank can have accounts of multiple customers.
4. Transaction
   1. Schema: `id: uuid`, `sender_account_id: uuid`, `receiver_account_id: uuid`, `amount: float`, `status: string`
   2. Relationships: Weak entity
      1. Sender and receiver accounts cannot be same.
      2. Two accounts can be of same or different banks.
      3. Two accounts can be of same customer.
      4. Status choices: `pending`, `processing`, `success`, `failed`
<!-- 5. Transaction Request
   1. Schema: `id: uuid`, `sender_account_id: uuid`, `receiver_account_id: uuid`, `amount: float`, `status: string`
   2. Relationships: Weak entity
      1. Sender and receiver accounts cannot be same.
      2. Two accounts can be of same or different banks.
      3. Two accounts can be of same customer.
      4. Status choices: `pending`, `success`, `failed` -->


### Components
#### Frontend
1. Web app: Typescript, NextJS
2. User interface: TailwindCSS, DaisyUI
3. Visualizations: E-charts
4. Build tools: webpack, vite
5. Mobile / Desktop installable app: PWA
#### Backend
1. Architecture: Python microservices
2. Auth: JWT, OAuth, OpenIDConnect
3. REST API: FastAPI
4. Models and migrations: SQLAlchemy, Alembic, SQLModel
5. Database: PostgreSQL, MongoDB
6. Background tasks: aiojobs,  
7. Message queue: Rabbitmq
8. Caching: Redis, memcached
9. CI/CD: Github Actions
10. Containerization and orchestration: Docker, Kubernetes
11. Unit, load and stress testing: pytest, Locust
12. Log aggregation, monitoring and analytics: ELK, Prometheus, Loki, Grafana
13. Generative AI: Langchain, Agent, RAG

### User Flows
1. Bank
   1. New
   2. Find all (filter and pagination)
   3. Find one 
   4. 
2. Customer
   1. New
   2. Find all (filters and pagination)
   3. Find one
   4. Get all bank accounts
   5. Get all banks
   6. Get all transactions
3. Bank Account
   1. New
4. Transaction
   1. New

### Tasks
- FastAPI base
- Postgresql instance
- SQLAlchemy
- Alembic
- Models
- Migrations
- Unit tests