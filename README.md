# 📝 Task Manager (Django + HTMX)

A simple, responsive Web application designed for managing personal projects and tasks effectively without full-page reloads, built using Django and HTMX.

---

## ✨ Features

- **Project Management (CRUD):** Create, edit, and delete TODO lists (projects) dynamically.
- **Task Management (CRUD):** Add tasks, edit details (title, deadline, priority), toggle completion status (`completed`), and delete tasks.
- **Single Page Application (SPA) Experience:** Instant AJAX interactions powered by **HTMX** with zero custom JS boilerplate.
- **User Authentication:** Secure access control via `django-allauth`. Users can only access and manage their own projects and tasks.
- **Responsive UI:** Clean, mobile-friendly layout built with Bootstrap 5.

---

## 🛠 Tech Stack

- **Backend:** Python 3.13, Django 5.2
- **Frontend:** HTML5, CSS3 (Bootstrap v5.3), HTMX
- **Authentication:** `django-allauth`
- **Database:** PostgreSQL / SQLite
- **Containerization:** Docker & Docker Compose
- **Code Quality:** Ruff (Linter & Formatter), djhtml, pre-commit

---

## 🚀 Getting Started (Local Setup via Docker Compose)

Follow these steps to build and launch the application locally.

### Prerequisites

Ensure you have installed:
- Docker Engine & Docker Compose
- Git

---

### Step 1. Clone the Repository

git clone <your-repository-url>
cd <repository-folder>

---

### Step 2. Set Up Environment Variables

Create a .env file in the root directory:

cp .env.example .env

---

### Step 3. Build and Start Container Services

Run Docker Compose to build images and launch containers in detached mode:

docker compose up -d --build

---

### Step 4. Run Database Migrations

Apply database schema migrations inside the running container:

docker compose exec web python manage.py migrate

---

### Step 5. Create Django Superuser

Create an administrative account to access the Django admin panel:

docker compose exec web python manage.py createsuperuser

---

### Step 6. Access the Application

Open your browser and navigate to:
- Web App: http://localhost:8000
- Django Admin: http://localhost:8000/admin/

---

## 🧪 Running Tests

Automated unit tests cover Project & Task CRUD operations, validation rules, HTMX responses, and user authorization/data isolation.

### Run Tests via Docker (Recommended)

docker compose exec web uv run python manage.py test

### Run Tests Locally

python manage.py test

---

## 🛠 Useful Docker Management Commands

* View application logs in real-time:
  docker compose logs -f

* Stop running containers:
  docker compose down

* Stop containers and remove volumes (database reset):
  docker compose down -v

* Restart application container:
  docker compose restart web

---

## 🧰 Code Quality & Formatting Tools

Project code consistency and quality are enforced using Ruff and djhtml.

### Manual Linting and Formatting Commands

* Ruff (Python Linter):
  docker compose exec web ruff check .

* Ruff (Python Formatter):
  docker compose exec web ruff format .

* djhtml (Django Templates Formatter):
  docker compose exec web djhtml templates/

---

### Setting Up Pre-commit Hooks

To automatically check and format code before every git commit:

1. Install pre-commit locally (or via uv):
   pip install pre-commit
   # or via uv:
   uv add --dev pre-commit

2. Install git hooks:
   pre-commit install

3. Run hooks against all files manually:
   pre-commit run --all-files

---

## 📄 License

Developed for educational and technical assessment purposes.