# fastapi_project

Here’s a ready-to-use README.md for your FastAPI project:



## Overview
This is a small FastAPI project demonstrating:
- 3 API routes
- Helper functions separated from routes
- 9+ automated tests (unit tests)
- GitHub Actions CI for test automation

## Project Structure

fastapi_project/
├── app/
│   ├── init.py
│   ├── main.py
│   ├── routes.py
│   └── helpers.py
├── tests/
│   ├── init.py
│   ├── test_helpers.py
│   └── test_routes.py
├── .github/
│   └── workflows/
│       └── test.yml
├── requirements.txt
├── pytest.ini
└── README.md

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

Install dependencies:

pip install -r requirements.txt

Start server:

uvicorn app.main:app --reload

Open browser at http://127.0.0.1:8000/docs to see Swagger UI.

Running Tests

pytest

All tests target helper functions to avoid using TestClient.

CI with GitHub Actions
	•	Tests run automatically on every push or pull request to main.
	•	Workflow file: .github/workflows/test.yml

Proof

![CI Test Passing Screenshot] https://i.postimg.cc/t4KSsB10/pythontesr.png

Notes
	•	Logic is separated into helpers.py to allow unit testing without API calls.
	•	Routes just call helper functions.

You can save this as `README.md` and later replace `actions-proof.png` with an actual screenshot of your workflow run.  

Do you want me to create a **ready folder structure with all files** for copy-paste?