# 🚀 FastAPI + Flask Learning Project

This repository is a hands-on learning project for building RESTful APIs using **FastAPI** and **Flask**. It explores routing, data validation, database integration with SQLAlchemy, and basic user authentication with password hashing.

---

## 📁 Table of Contents
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [API Overview](#api-overview)
- [Tech Stack](#tech-stack)
- [Notes](#notes)

---

## 📁 Project Structure
- `blog/` - Contains the FastAPI application and related files.
- `flask_app.py` - The main entry point for the Flask application.
- `requirements.txt` - Lists the dependencies for the project.
- `blog.db` - SQLite database file.

---

## 📦 Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/mrastatine-fastapi-learning-.git
    cd mrastatine-fastapi-learning-
    ```

2. **Set up a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the FastAPI application**:
    ```bash
    uvicorn blog.main:app --reload
    ```

5. **Run the Flask application**:
    ```bash
    python flask_app.py
    ```

---

## 📘 API Overview

### ✅ FastAPI Endpoints
- **GET /** – Home route
- **GET /blog** – List blogs (published/unpublished via query)
- **GET /blog/{id}** – Retrieve blog by ID
- **POST /blog** – Create a blog
- **PUT /blog/{id}** – Update a blog
- **DELETE /blog/{id}** – Delete a blog
- **POST /user** – Create user with password hashing

### ✅ Flask Endpoints
- **GET /** – Home route
- **GET /get-user/<user_id>** – Get mock user data
- **POST /create-user** – Create mock user from request body

---

## 🗃️ Tech Stack
- ⚡ FastAPI
- 🌐 Flask
- 🧬 SQLAlchemy (SQLite backend)
- 🛡️ Passlib + bcrypt (for password hashing)
- 📦 Pydantic (for validation)

---

## 📌 Notes
- The FastAPI app uses a local SQLite database (`blog.db`).
- All blog and user data are persisted via SQLAlchemy ORM.
- Passwords are hashed before storage using bcrypt.
- Project is modular and follows basic clean code practices.
