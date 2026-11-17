
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Telecom Prepaid Plan API",
    description="API for managing prepaid mobile plans",
    version="1.0"
)

plans = [
    {"id": 1, "name": "Basic Plan", "price": 199, "data": "2GB/day", "validity": 28},
    {"id": 2, "name": "Standard Plan", "price": 299, "data": "3GB/day", "validity": 28},
    {"id": 3, "name": "Premium Plan", "price": 499, "data": "2GB/day", "validity": 84},
    {"id": 4, "name": "Student Plan", "price": 149, "data": "1GB/day", "validity": 28}
]

class Plan(BaseModel):
    id: int
    name: str
    price: int
    data: str
    validity: int

@app.get("/")
def home():
    return {"message": "Welcome to Telecom Prepaid Plan API"}

@app.get("/plans")
def get_plans():
    return plans

@app.get("/plans/search")
def search_plans(max_price: int):
    return [p for p in plans if p["price"] <= max_price]

@app.get("/plans/filter")
def filter_plans(validity: int):
    return [p for p in plans if p["validity"] == validity]

@app.post("/plans")
def add_plan(plan: Plan):
    if any(p["id"] == plan.id for p in plans):
        return {"error": "Plan ID already exists"}

    plans.append(plan.model_dump())
    return {"message": "Plan added successfully", "plan": plan}
