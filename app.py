from flask import Flask, request, jsonify
from flasgger import Swagger
from datetime import datetime

app = Flask(__name__)

# Configure Swagger
swagger = Swagger(app)

# Simple in-memory storage
employees = []
customers = []
products = []
orders = []
productions = []

# Routes
@app.route('/employees', methods=['POST'])
def create_employee():
    """
    Create a new employee
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            position:
              type: string
          required:
            - name
            - position
    responses:
      201:
        description: Employee created successfully
      400:
        description: Invalid input
    """
    try:
        data = request.get_json()
        employee = {
            'id': len(employees) + 1,
            'name': data['name'],
            'position': data['position'],
            'hire_date': datetime.utcnow().isoformat()
        }
        employees.append(employee)
        return jsonify(employee), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/employees', methods=['GET'])
def get_employees():
    """
    Get all employees
    ---
    responses:
      200:
        description: List of all employees
    """
    return jsonify(employees)

@app.route('/customers', methods=['POST'])
def create_customer():
    """
    Create a new customer
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            email:
              type: string
            phone:
              type: string
          required:
            - name
            - email
    responses:
      201:
        description: Customer created successfully
      400:
        description: Invalid input or email already exists
    """
    try:
        data = request.get_json()
        # Check for duplicate email
        if any(c['email'] == data['email'] for c in customers):
            return jsonify({'error': 'Email already exists'}), 400
            
        customer = {
            'id': len(customers) + 1,
            'name': data['name'],
            'email': data['email'],
            'phone': data.get('phone', '')
        }
        customers.append(customer)
        return jsonify(customer), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/customers', methods=['GET'])
def get_customers():
    """
    Get all customers
    ---
    responses:
      200:
        description: List of all customers
    """
    return jsonify(customers)

if __name__ == '__main__':
    app.run(debug=True)
