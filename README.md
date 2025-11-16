# Flask DevOps Lab

A Flask REST API demonstrating DevOps practices with GitHub Actions CI/CD pipelines.

## API Endpoints

### GET /
Returns a simple greeting message.
- **Response**: `Hello, DevOps World!`

### POST /echo
Echoes back the JSON payload sent in the request.
- **Request Body**: Any valid JSON
- **Response**: Same JSON payload (Status: 201)
- **Example**:
  ```bash
  curl -X POST http://localhost:5000/echo -H "Content-Type: application/json" -d '{"msg": "ping"}'
  ```

### PUT /reverse
Reverses a text string provided in the JSON payload.
- **Request Body**: `{"text": "your string here"}`
- **Response**: `{"original": "your string here", "reversed": "ereh gnirts ruoy"}`
- **Example**:
  ```bash
  curl -X PUT http://localhost:5000/reverse -H "Content-Type: application/json" -d '{"text": "hello"}'
  ```

### GET /jokes
Returns a random programming joke.
- **Response**: `{"joke": "Why do programmers prefer dark mode? ..."}`
- **Example**:
  ```bash
  curl http://localhost:5000/jokes
  ```

### GET /storage
Returns all items currently stored in memory.
- **Response**: `{"items": [...], "count": 0}`

### POST /storage
Adds an item to the in-memory storage.
- **Request Body**: `{"item": "your item here"}`
- **Response**: `{"message": "Item added", "item": "your item here"}` (Status: 201)
- **Example**:
  ```bash
  curl -X POST http://localhost:5000/storage -H "Content-Type: application/json" -d '{"item": "todo task"}'
  ```

### DELETE /storage
Clears all items from storage.
- **Response**: `{"message": "Cleared X items", "count": X}`
- **Example**:
  ```bash
  curl -X DELETE http://localhost:5000/storage
  ```

## GitHub Actions Workflows

This repository includes three CI/CD pipelines:

### 1. Test Pipeline (test.yml)
- **Trigger**: On every push and pull request
- **Python Versions**: 3.10, 3.11, 3.12
- **Steps**:
  - Checkout code
  - Set up Python environment
  - Install dependencies
  - Run pytest with code coverage
  - Upload coverage reports to Codecov

### 2. Linting Pipeline (init.yml)
- **Trigger**: On every push and pull request
- **Python Versions**: 3.10, 3.11, 3.12
- **Steps**:
  - Checkout code
  - Set up Python environment
  - Install Flake8
  - Run Flake8 linter on Python files

### 3. CodeQL Security Analysis (codeql.yml)
- **Trigger**: On push to main branch and pull requests
- **Purpose**: Automated security vulnerability scanning
- **Language**: Python

## Running Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Run tests:
   ```bash
   pytest test_app.py
   ```

4. Run tests with coverage:
   ```bash
   pytest --cov=app test_app.py
   ```

5. Run linting:
   ```bash
   flake8 app.py test_app.py
   ```

## Implementation Notes

### Endpoints Implemented
- **POST /echo**: Simple echo endpoint as specified in Part 8
- **PUT /reverse**: String reversal endpoint demonstrating PUT method
- **GET /jokes**: Fun endpoint that returns random programming jokes
- **GET/POST/DELETE /storage**: Complete CRUD-like storage system demonstrating all HTTP methods

### Tests Added
- `test_echo()`: Basic echo test as specified
- `test_echo_complex()`: Tests echo with complex nested JSON
- `test_reverse()`: Tests string reversal functionality
- `test_reverse_missing_field()`: Tests error handling
- `test_get_jokes()`: Tests joke endpoint
- `test_storage_workflow()`: Comprehensive test of GET/POST/DELETE workflow
- `test_storage_missing_item()`: Tests error handling for storage

### Issues Encountered
No major issues encountered. The implementation was straightforward:
- All tests pass with 100% code coverage
- Flake8 linting passes without warnings
- CodeQL security scan shows no vulnerabilities
- All workflows execute successfully across Python 3.10, 3.11, and 3.12
