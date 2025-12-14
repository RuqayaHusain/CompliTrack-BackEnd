# CompliTrack – Backend

## 📝 Overview

This repository contains the **FastAPI backend** for **CompliTrack**, a compliance and license tracking system designed for SMEs in Bahrain.  
The backend provides secure authentication, RESTful APIs, and database management for users, businesses, licenses, and compliance tasks.

---

## 🚀 Getting Started

### 🔗 Links
- **Frontend Repository:** [Frontend Repo](https://github.com/RuqayaHusain/CompliTrack-FrontEnd)

---

## 🛠️ Technologies Used

- FastAPI
- Python 3.9+
- PostgreSQL
- SQLAlchemy ORM
- Pydantic (v2)
- JWT Authentication
- Uvicorn

---

## 🧱 Core Entities

- **User** – Authenticated system users
- **Business** – SME businesses owned by users
- **License** – Business licenses with expiry dates
- **Compliance Task** – Compliance obligations and deadlines

---

## 🔐 Authentication & Authorization

- JWT-based authentication
- Secure login and registration
- Protected routes
- Only authenticated users can create, update, or delete data

---

## 🔁 API Routes (Sample)

### Authentication
- `POST /api/auth/register`
- `POST /api/auth/login`

### Users
- `GET /api/users`

### Businesses
- `POST /api/businesses`
- `GET /api/businesses`

### Licenses
- `POST /api/licenses`
- `GET /api/licenses`

### Compliance Tasks
- `POST /api/tasks`
- `GET /api/tasks`
