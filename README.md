
# 📱 Telecom Prepaid Plan API

<div align="center">

### A RESTful API for Managing Telecom Prepaid Plans

Built with Python and FastAPI 🚀

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge)
![API](https://img.shields.io/badge/REST-API-purple?style=for-the-badge)

</div>

---

## 📌 Project Overview

The **Telecom Prepaid Plan API** is a Python-based REST API developed using FastAPI.

It provides endpoints to manage fictional telecom prepaid plans, retrieve available plans, search plans based on price, and filter plans based on validity.

This project demonstrates the fundamentals of REST API development, request handling, data validation, and API documentation.

## 🎯 Objectives

- Understand REST API architecture.
- Develop API endpoints using FastAPI.
- Handle HTTP GET and POST requests.
- Validate request data using Pydantic.
- Explore API testing through Swagger UI.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | Backend API framework |
| Pydantic | Data validation |
| Swagger UI | API documentation and testing |

## ✨ Features

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/plans` | Retrieve all prepaid plans |
| GET | `/plans/search` | Search plans by maximum price |
| GET | `/plans/filter` | Filter plans by validity |
| POST | `/plans` | Add a new prepaid plan |

## 📂 Project Structure

```text
telecom-prepaid-plan-api/
│
├── main.py
├── requirements.txt
└── README.md
```

*Note: Update this structure if your repository contains additional files or folders.*

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Navanthika13/telecom-prepaid-plan-api.git
```

### 2. Navigate to the project directory

```bash
cd telecom-prepaid-plan-api
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
uvicorn main:app --reload
```

### 5. Open the API documentation

Visit:

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows you to explore and test the available API endpoints.

## 🔍 API Testing

Example API request:

```http
GET /plans
```

Example search request:

```http
GET /plans/search?max_price=299
```

*Note: The query parameter name and example values should match your actual implementation.*

## 📸 API Documentation Preview

The API can be explored and tested through FastAPI's interactive Swagger UI.

## 📚 Concepts Learned

- REST API development
- HTTP methods (GET and POST)
- API routing
- Request and response handling
- Data validation using Pydantic
- Interactive API documentation

## 🚧 Future Improvements

- Database integration using MySQL or PostgreSQL
- JWT-based authentication
- Docker containerization
- Redis caching
- Automated API testing
- Improved error handling

## 👩‍💻 Developer

**Navanthika**

Information Technology Student | Aspiring Software Developer

[GitHub Profile](https://github.com/Navanthika13)

---

<div align="center">

### 💜 Built with Python & FastAPI

**Learn | Build | Improve**

</div>
