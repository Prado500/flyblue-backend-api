# ✈️ FlyBlue API - Backend Architecture

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql)
![Azure DevOps](https://img.shields.io/badge/Azure_DevOps-0078D7?style=for-the-badge&logo=azuredevops)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker)

## 📋 Context & Contributions

This repository hosts the backend for **FlyBlue**, a flight management system developed as a collaborative academic project. The architecture was designed to be scalable, asynchronous, and secure.

### 👨‍💻 My Contributions (David De Los Reyes - Backend Engineer)
As the lead for **Architecture & Deployment**, my specific contributions were:
* **Database Stability (SQLAlchemy):** Refactored the data models to resolve critical circular dependencies and ensured seamless automatic table generation from Python code.
* **Core Business Logic:** Implemented key endpoints for flight scheduling, inventory management, and booking workflows.
* **CI/CD & DevOps:** Configured the Continuous Integration pipeline in **Azure DevOps**, automating containerized deployments to Azure App Service.
* **Debugging:** Troubleshooting and resolving integration conflicts between Pydantic schemas and the database connector.

*(Note: The JWT Authentication module and initial project boilerplate were developed in collaboration with teammate S. Manchola).*

---

## 🚀 System Overview

Flight management system developed with **FastAPI** (Asynchronous mode), **PostgreSQL**, and **JWT** authentication. The project features a fully automated **CI/CD** workflow using **Azure DevOps**, deploying to **Azure App Service for Containers**.

### Key Features
- **JWT Authentication:** Role-based access control (Client & Admin).
- **Flight Management:** Search, booking, and payment processing logic.
- **Admin Panel:** Endpoints to manage cities, aircraft, and baggage types.
- **PostgreSQL Database:** Docker-ready relational database.
- **Auto-Documentation:** Swagger/OpenAPI available at `/docs`.
- **Automated CI/CD:** Azure DevOps Pipelines.
- **Multi-Environment Deployment:** Dev, Test, Prod.

## ☁️ Deployed Environments (CI/CD)

The pipeline automatically deploys to specific environments based on the Git branch:

| Environment | Branch | Base API URL |
| :--- | :--- | :--- |
| **Development** | `dev` | `flyblue-api-server-dev...azurewebsites.net` |
| **Testing** | `test` | `flyblue-api-server-test...azurewebsites.net` |
| **Production** | `main` | `flyblue-api-server-main...azurewebsites.net` |

## 🛠️ Tech Stack

* **Language:** Python 3.11+
* **Framework:** FastAPI (Asynchronous)
* **ORM:** SQLAlchemy
* **Database:** PostgreSQL
* **Containerization:** Docker & Docker Compose
* **Validation:** Pydantic

## ⚙️ Local Installation & Setup

### 1. Clone the repository
```bash
git clone [https://github.com/Prado500/flyblue-backend-api.git](https://github.com/Prado500/flyblue-backend-api.git)
cd flyblue-backend-api
```

### 2. Configure Environment Variables
```bash
# Create .env file based on the example
cp .env.example .env
```

### 3. Run with Docker (Recommended)
```bash
docker-compose up -d --build
```
**API:** http://localhost:8000

**Docs:** http://localhost:8000/docs

**DB:** localhost:5432



## 👤 User Registration Boilerplate

**To register a new user, you can send this JSON template within the request body (test scenario)**
```JSON
{
  "nombre": "flyblue-test",
  "correo": "flyblue-test@flyblue.com",
  "contraseña": "pass"
}
```
**NOTE:** For login, you can use the same JSON excluding the nombre field. After loging in, the API will provide an user-specific token.



## 📚 Main Endpoints

🔓**Public**

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **POST** | `/v1/auth/register` | `Register new user (Use registration boilerplate provided above)` |
| **POST** | `/v1/auth/login` | `Login (Obtain Bearer Token)` |



🔒**Private**

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/v1/vuelos` | `Search flights (Filters: origin, destination, date)` |
| **POST** | `/v1/cliente/reservas` | `Create a new booking` |
| **POST** | `/v1/admin/vuelos` | `(Admin) Create a new flight route` |


(For the full list of endpoints, JSON schemas, and API testing, visit the interactive documentation at /docs when running the project).



## 🔒 Security

**JWT Authentication:** Non-expiring tokens for testing convenience.

**Roles:** Client / Administrator.

**Hashing:** Passwords encrypted using bcrypt.

Backend Architecture optimized by **David De Los Reyes.**


