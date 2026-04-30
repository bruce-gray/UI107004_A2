# UI107004_A2
## UI107004 - Assessment 2 - Database Solution Project with Security Review

# Library Inventory System
A database-backed API for managing library book inventory and loans. Built with MySQL and Python (Flask), serving data via JSON.

- **app.py** - Flask application containing all API endpoints
- **sql/schema.sql** - Database schema including tables and constraints
- **sql/seed.sql** - Sample data for all tables
- **sql/procedure.sql** - Stored procedure for book checkout

## Requirements
- MySQL installed https://www.mysql.com/downloads/
- Python installed https://www.python.org/downloads/
- Flask and mysql-connector-python installed (see below)

## Setting up the database
Open each SQL file in MySQL Workbench and run in the following order:

**1. Create the schema:**
```bash
schema.sql
```
**2. Populate with sample data:**
```bash
seed.sql
```
**3. Create the stored procedure:**
```bash
procedure.sql
```

## Installing dependencies
```bash
pip install flask mysql-connector-python
```

## Running the API
Run from the root of the project:
```bash
python app.py
```
The API will be available at `http://127.0.0.1:5000`

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/books` | Returns all available books as JSON |
| POST | `/checkout` | Checks out a book to a member via stored procedure |
| GET | `/loans` | Returns all active loans as JSON |

## Checkout endpoint usage
The `/checkout` endpoint requires a POST request and cannot be tested in a browser. Use curl in Git Bash:

**Successful checkout (available book):**
```bash
curl -X POST http://127.0.0.1:5000/checkout -H "Content-Type: application/json" -d '{"book_id": 2, "member_id": 1}'
```

**Error response (unavailable book):**
```bash
curl -X POST http://127.0.0.1:5000/checkout -H "Content-Type: application/json" -d '{"book_id": 1, "member_id": 1}'
```