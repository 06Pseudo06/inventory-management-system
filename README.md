# 🧾 Inventory Management System (Django)

A **role-based inventory management system** built with Django, focused on **data integrity**, **transactional correctness**, and **clean backend architecture**, with a functional dashboard UI for operational use.

> **Status:** v4 complete & stable  
> Designed as a production-minded learning project showcasing backend engineering fundamentals


## 🔍 Project Overview

This project manages inventory items and tracks all stock changes through a **transaction-driven model**.  
Instead of directly editing stock values, every change is recorded as a transaction, ensuring:

- **Traceability**
- **Auditability**
- **Consistent business rules**

The system includes a dashboard for operational users and integrates **Django Admin** for secure management tasks.


## ✨ Key Features

### 📦 Inventory Management
- Item creation with stock quantity tracking
- Minimum stock threshold support
- Soft-deletion (items can be deactivated, not destroyed)
- Visual identification of low-stock items

### 🔄 Transaction System
- Stock **IN / OUT** handled exclusively via transactions
- Automatic quantity updates
- Prevention of negative inventory
- Immutable transaction history

### 📊 Dashboard
- Inventory summary statistics
- Low-stock items table
- Recent transaction overview
- Stock-level visualization using **Chart.js**

### 👥 Role-Based Access Control
- **Admin (Superuser)**
  - Full system access
  - Django admin panel
  - Inventory & transaction management
- **Staff**
  - Dashboard access
  - Inventory visibility
  - Transaction creation
- **Unauthorized users**
  - No access

### 🧭 Usability & UI
- Clean, consistent table styling
- Paginated item listing for scalability
- Role-aware navigation (admin links shown only to admins)



## 🧱 Architecture & Design Decisions

The project follows a **layered and maintainable architecture**:

- **Models** — Define data structures and relationships  
- **Views** — Handle HTTP requests and orchestration  
- **Templates** — Minimal, functional UI  
- **Admin** — Safe management interface  
- **Permissions** — Explicit role-based access control  

### Why this matters:
- Prevents accidental data corruption
- Keeps business rules centralized
- Makes the system easy to extend and maintain



## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Database (v1):** SQLite (development)
- **Authentication:** Django built-in auth system
- **Frontend:** Django templates, HTML, CSS
- **Charts:** Chart.js
- **Version Control:** Git & GitHub



## ▶️ Running Locally

### Clone the repository
```bash
git clone https://github.com/06Pseudo06/inventory-management-system.git
cd inventory-management-system
````

### Create and activate virtual environment

```bash
python -m venv env
env\Scripts\activate   # Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Apply migrations

```bash
python manage.py migrate
```

### Create admin user

```bash
python manage.py createsuperuser
```

### Run development server

```bash
python manage.py runserver
```

**Access:**

* **App UI:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **Admin panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)



## 🚧 Current Limitations (Intentional)

* SQLite used for development only
* Minimal UI (function-first design)
* No deployment configuration in v1
* Search & advanced filtering planned

These are **deliberate scope decisions**, not architectural flaws.


## 🔮 Planned Enhancements

* Item search & filtering
* PostgreSQL integration
* Production environment configuration

## 🎯 What This Project Demonstrates

* Backend system design thinking
* Safe data mutation via transactions
* Role-based authorization
* Django ORM & admin proficiency
* Pagination & scalable UI patterns
* Clean Git workflow & project closure


## 👤 Author

Built as a **learning-driven, production-oriented project** to demonstrate real-world backend development practices using Django.


### 📌 Note

This project is intentionally scoped to demonstrate **correctness, structure, and extensibility**, rather than UI-heavy features.
Future enhancements are planned and documented.

