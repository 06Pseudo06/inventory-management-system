# INVENTORY MANAGEMENT SYSTEM (V1)

A Django-based inventory management system designed with data integrity, role-based access, & transactional accuracy at its core.  
This project focuses on building a realistic backend architecture suitable for real-world inventory workflows.  

⚠️ Project Status: Under active development.  
> v1 represents the core system with validated business logic and access control.  


## OVERVIEW

This system manages inventory items and tracks all stock changes through immutable transactions.  
Instead of directly modifying stock values, every inventory update is recorded as a transaction, ensuring auditability and correctness.  
The project is intentionally backend-focused, prioritizing clean architecture, correctness, and scalability over UI complexity.  


## KEY FEATURES (V1)

### Inventory Core:-   
• Item management with current stock tracking  
• Minimum stock threshold support  
• Soft deactivation of items (no destructive deletes)  

### Transaction System:- 
• Stock IN / OUT handled exclusively via transactions  
• Automatic stock updates  
• Prevention of negative inventory  
• Immutable transaction history  

### Role-Based Access Control:- 
• Admin  
&nbsp;&nbsp;&nbsp;&nbsp;• Full access  
&nbsp;&nbsp;&nbsp;&nbsp;• Create/edit items  
&nbsp;&nbsp;&nbsp;&nbsp;• View all data  
• Staff  
&nbsp;&nbsp;&nbsp;&nbsp;• Create inventory transactions  
&nbsp;&nbsp;&nbsp;&nbsp;• View inventory  
• Unauthorized users  
&nbsp;&nbsp;&nbsp;&nbsp;• No access  

### Admin Safety :-
• Direct stock editing disabled  
• Transactions are append-only  
• All mutations routed through service-layer logic  


## ARCHITECTURE HIGHLIGHTS

The project follows a layered architecture:  
&nbsp;&nbsp;• Models → Define data and relationships  
&nbsp;&nbsp;• Services → Enforce business rules and invariants  
&nbsp;&nbsp;• Views → Handle HTTP requests only  
&nbsp;&nbsp;• Admin → Safe operational interface  
&nbsp;&nbsp;• Permissions → Explicit and enforced  
  
This separation ensures:  
&nbsp;&nbsp;• Maintainability  
&nbsp;&nbsp;• Testability  
&nbsp;&nbsp;• Protection against accidental data corruption  

  
## TECH STACK

• Backend: Django (Python)  
• Database (v1): SQLite (development)  
• Authentication: Django built-in auth system  
• Frontend: Django templates (minimal UI)  
• Version Control: Git & GitHub  


## RUNNING LOCALLY (DEVELOPMENT)

 ### Clone repository
`git clone https://github.com/<your-username>/inventory-management-system.git`  
`cd inventory-management-system`

### Create virtual environment
`python -m venv env`  
`env\Scripts\activate  # Windows`

### Install dependencies
`pip install -r requirements.txt`  

### Apply migrations
`python manage.py migrate`  

### Create admin user
`python manage.py createsuperuser`  

### Run server
`python manage.py runserver`  

Access:  
Admin panel → http://127.0.0.1:8000/admin/  
Inventory UI → http://127.0.0.1:8000/  


## CURRENT LIMITATIONS (INTENTIONAL)

• SQLite used only for development  
• Minimal frontend UI  
• No deployment configuration in v1  
• No analytics dashboard yet  
These are planned upgrades, not design gaps.  

## ROADMAP (NEXT PHASE)

Planned enhancements include:  

• PostgreSQL integration  
• Environment-based production settings  
• Deployment (Render / Railway)  
• Low-stock alerts and analytics  
• Improved UI and reporting  
• Automated tests  

## PROJECT STATUS

🚧 **Under Construction**
This repository represents v1 (core system).  
Further development will focus on making the system production-ready and deployable.  

## AUTHOR

*Built as a learning-driven yet production-oriented project to understand real backend system design using Django.*




