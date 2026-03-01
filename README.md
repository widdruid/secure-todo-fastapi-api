# ✅ Secure Todo API — FastAPI Backend

A secure RESTful Todo API built using **FastAPI** implementing JWT authentication, request validation, and structured backend architecture.

This API serves as the backend for the Vue 3 Todo Application.

Frontend repository:

👉 https://github.com/widdruid/secure-todo-vue-ui

---

## 🚀 Tech Stack

- FastAPI
- SQLite
- SQLAlchemy ORM
- JWT Authentication
- Pydantic Validation
- Python 3

---

## 🎯 Project Objective

Designed to demonstrate:

✅ RESTful API design  
✅ Authentication & Authorization  
✅ Secure client-server communication  
✅ Request validation  
✅ Clean backend architecture  

---

## 🔐 Security Features

### Authentication
- JWT Access Tokens
- Password hashing using bcrypt
- Token-based authorization

---

### Encryption
- Passwords hashed before storage
- HTTPS-ready API structure
- Secure token verification

---

### Validation
Using **Pydantic schemas**:

- Request body validation
- Data type enforcement
- Automatic error responses

---

## 🧱 Backend Architecture
app/
│
├── main.py
├── database.py
├── models/
├── schemas/
├── routes/
├── services/
├── core/
│ ├── security.py
│ └── config.py


---

## 📡 API Endpoints

### Authentication

| Method | Endpoint | Description |
|------|------------|------------|
| POST | /register | Register user |
| POST | /login | Login user |

---

### Todos

| Method | Endpoint | Description |
|------|------------|------------|
| GET | /todos | Get all todos |
| GET | /todos/{id} | Get todo |
| POST | /todos | Create todo |
| PUT | /todos/{id} | Update todo |
| DELETE | /todos/{id} | Delete todo |

---

## ⚙️ Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
http://localhost:8000
