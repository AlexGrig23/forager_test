# Test task for FORAGER

## Description
Web application in FastAPI for validate email and phone number

## Basic Requirements
 - API for validate email and phone number

---
## Installation
**1. Clone the repository:**

   ```shell
   git clone https://github.com/AlexGrig23/test.git
   ```

  Create virtual env.

   ```shell
   python -m venv venv
   ```
  
   Activate virtual env.
   
   on Windows: 
   ```shell
   cd venv/Scripts
   ```
   ```shell
   ./activate
   ```
  on Linux or Mac
   ```shell
   source venv/bin/activate
   ```

**2. Install dependencies**

Navigate to the project directory:
   ```shell
   cd forager_test (root)
   ```

   ```shell
    pip install -r requirements.txt
    ```
   ```
   
**3. Run app**

   ```shell
   uvicorn main:app --reload
   ```
   Starting development server at  http://127.0.1:8000/
  
	
## Usage

**1. API Documentations**
 
Interactive API documentation available at

 http://127.0.1:8000/docs/


## Technologies

- Python 3.11
- FastAPI
- Pydantic
- Uvicorn
- wemake-python-styleguide


## License
MIT License

Created by Alex Grig
email:alexgrig.cyber@gmail.com