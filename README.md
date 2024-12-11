# Factory Management System API

This is a Flask-based API for managing factory operations, including employees, products, customers, orders, and production tracking. The API is fully documented using Swagger/OpenAPI specification.

## Features

- Employee Management
- Product Management
- Customer Management
- Order Tracking
- Production Monitoring
- Full Swagger Documentation

## Setup and Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

## API Documentation

Once the application is running, you can access the Swagger documentation at:
```
http://localhost:5000/docs
```

The documentation includes:
- Detailed endpoint descriptions
- Request/Response examples
- Error handling information
- Model schemas

## Models

The system includes the following models:
- Employee: Manage factory employees
- Product: Track products and their details
- Customer: Manage customer information
- Order: Track customer orders
- Production: Monitor production activities

## Error Handling

The API includes comprehensive error handling, particularly for the Customer model endpoints. Common error scenarios include:
- Invalid input data
- Duplicate email addresses
- Missing required fields
- Server errors

## Testing

You can test the API endpoints using the interactive Swagger UI or any API testing tool like Postman.
