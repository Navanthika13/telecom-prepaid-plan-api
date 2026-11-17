# Telecom Prepaid Plan API

## Project Description
A FastAPI-based REST API for managing fictional telecom prepaid plans.

## Technologies
- Python
- FastAPI
- Pydantic
- Swagger UI

## Features
1. GET / - Welcome message
2. GET /plans - View all plans
3. GET /plans/search - Search plans by maximum price
4. GET /plans/filter - Filter plans by validity
5. POST /plans - Add a new prepaid plan

## Run the Project

Install dependencies:

pip install -r requirements.txt

Start the server:

uvicorn main:app --reload

Open Swagger documentation:

http://127.0.0.1:8000/docs

## Project Status
Basic working prototype. Advanced features such as database integration,
JWT authentication, Docker, Redis and automated testing are not yet implemented.