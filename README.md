# FastAPI Course Catalog Management System

A REST API project built with Python, FastAPI, SQLAlchemy, and Pydantic to manage courses and student enrollments.

## Features

- Course management
- Student enrollment management
- REST API endpoints
- Database integration

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- MySQL

## Requirements

- Python 3.10 or newer
- MySQL Server
- pip

## Setup Instructions

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd FastAPI_Project
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Configure the database

Create a `.env` file with your own database connection settings.
Never share database passwords publicly.

### 6. Run the application

```bash
uvicorn main:app --reload
```

### 7. Open the API documentation

Visit:

http://127.0.0.1:8000/docs

## Note

Configure the database before running the application.