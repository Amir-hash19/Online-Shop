# 🛒 Online Shop

A server-side rendered e-commerce web application built with Django.  
The project is containerized using Docker and deployed on Render.

---

## 🖼️ Project Preview

![Landing Page Screenshot](readme/landing.png)

> Replace this placeholder with a screenshot of the homepage / landing page.

---

## 🚀 Features

- Server-side rendering (Django Templates)
- User authentication system
- Product management (CRUD)
- Category management
- Shopping cart functionality
- Order processing workflow
- PostgreSQL database integration
- Debug tools for development
- Clean modular Django architecture

---

## 🧰 Tech Stack

### Backend
- Django 4.2.27
- ASGI / WSGI (asgiref 3.11.0)
- Python 3.x

### Database
- PostgreSQL (psycopg 3.3.2 / psycopg-binary 3.3.2)

### Utilities
- python-decouple (environment variables management)
- sqlparse
- typing_extensions

### Media Handling
- Pillow

### Development Tools
- django-debug-toolbar
- black (code formatter)
- isort (import sorting)
- flake8 (linting)

---

## 🐳 Dockerized Setup

This project is fully containerized using Docker.

### Build Image
```bash id="1nq8pd"
docker build -t online-shop .





## ▶️ How to Run (Docker)

### 1. Build Docker image
```bash
docker-compose up --build

docker-compose up

docker-compose down
