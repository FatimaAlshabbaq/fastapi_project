# fastapi_project

## Overview
This is a small FastAPI project :
- 3 API routes
- Helper functions separated from routes
- 9+ automated tests (unit tests)
- GitHub Actions CI for test automation

## Technologies Used
- *Python 3.11* – Programming language
- *FastAPI* – Web framework for API development
- *Uvicorn* – ASGI server to run FastAPI
- *Pytest* – Testing framework
- *HTTPX* – Optional, for making HTTP requests in tests
- *GitHub Actions* – CI/CD to automatically run tests on commit or PR


## API Routes
1. **GET /hello** – Returns `{"message": "Hello, World!"}`  
2. **GET /square/{number}** – Returns the square of a number, e.g., `{"number": 5, "square": 25}`  
3. **GET /reverse/{text}** – Returns the reversed string, e.g., `{"original": "abc", "reversed": "cba"}`  

## Running Locally
Activate virtual environment:
```bash
# Linux / Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
```
## Install dependencies:
```bash
pip install -r requirements.txt
```
## Start server:
```bash
uvicorn app.main:app --reload
```
Open browser at http://127.0.0.1:8000/docs to see Swagger UI.

## Running Tests
```bash
pytest
```

All tests target helper functions to avoid using TestClient.

## CI with GitHub Actions
•	Tests run automatically on every push or pull request to main.

•	Workflow file: .github/workflows/test.yml

[CI Test Passing Screenshot] https://i.postimg.cc/t4KSsB10/pythontesr.png

## Notes
•	Logic is separated into helpers.py to allow unit testing without API calls.

•	Routes just call helper functions.

