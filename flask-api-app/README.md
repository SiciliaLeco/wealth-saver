# Flask API Application

This is a simple Flask API application skeleton.

## Project Structure

```
flask-api-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   └── models.py
├── requirements.txt
├── config.py
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-api-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, use the following command:
```
flask run
```

Make sure to set the `FLASK_APP` environment variable to `app` before running the command.

## API Endpoints

- Define your API endpoints in `app/routes.py`.

## License

This project is licensed under the MIT License.