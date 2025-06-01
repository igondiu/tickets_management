# Simple FastAPI app using SQLModel  
SQLModel is based on Python type annotations, and powered by Pydantic and SQLAlchemy.  
The projects goal is to create a minimal robust and modern FastAPI application.  

## Project structure
```scss
tickets_management_backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py                # FastAPI app initialization and main routes
│   ├── database.py            # Database setup and session management
│   ├── models/                # SQLModel models
│   │   ├── __init__.py
│   │   └── ticket.py          # Ticket model
│   ├── schemas/               # Pydantic schemas for data validation
│   │   ├── __init__.py
│   │   └── ticket.py          # Ticket schemas
│   ├── routers/               # API endpoints
│   │   ├── __init__.py
│   │   └── endpoints/
│   │       ├── __init__.py
│   │       └── ticket.py      # Ticket endpoints
│   ├── kernels/               # CRUD operations mainly
│   │   ├── __init__.py
│   │   └── ticket.py          # Ticket CRUD operations
│   └── settings.py            # Configuration settings
│
├── tests/                     # Test files
│   ├── __init__.py
│   └── test_ticket.py         # Test cases for ticket API endpoints
│
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── .env                       # Environment variables
```

## This project is made to be used with **uv** for dependency management
Read more about **_uv_** on uv's official web page [here](https://docs.astral.sh/uv/) 
### Create virtual environment and install project dependencies
Uv needs to be installed on your computer before running the sync command, if you don't want to install uv, you can skip this step and go to the step where **venv** and **pip** is used instead of **uv**.  
Follow this to install uv: https://docs.astral.sh/uv/getting-started/installation/
```
uv sync --locked
```

### Not convinced by uv ? you are free to use venv and pip
1. Create virtual environment with this command:
```shell
python -m venv .venv
```
Activate venv  
On windows:
```shell
venv/bin/activate.bat
```
On Unix:
```shell
source venv/bin/activate
```

2. Install project dependencies with this command:
```shell
python -m pip install -r requirements.txt
```

## Database and data is managed using SQLModel
More about SQLModel on its official web page [here](https://sqlmodel.tiangolo.com/#sql-databases-in-fastapi)

## Logs
Logs are available in the folder tickets_management_backend/logs/*.log  
If something doesn't work as expected you can consult the logs

## Unit tests
Pytest was used to create the unit tests.
To run the unit tests execute this command:
```shell
python -m pytest tests/
```

## Run the application
To run the application, make sure you created virtual environment and installed project dependencies.  
Use this command to run the application:
```shell
python app/main.py
```
