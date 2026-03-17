from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# PostgreSQL connection
conn = psycopg2.connect(
    database="finance_db",
    user="postgres",
    password="YourPassowrd",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# Data model
class Expense(BaseModel):
    amount: float
    category: str
    description: str
    date: str


@app.post("/add-expense")
def add_expense(expense: Expense):

    cursor.execute(
        "INSERT INTO transactions (amount, category, description, transaction_date) VALUES (%s,%s,%s,%s)",
        (expense.amount, expense.category, expense.description, expense.date)
    )

    conn.commit()

    return {"message": "Expense Added"}


@app.get("/expenses")
def get_expenses():

    cursor.execute("SELECT * FROM transactions")

    return cursor.fetchall()
