from flask import Flask, jsonify, request

app = Flask(__name__)

employees = [
    {"id": 1, "name": "Rahul", "role": "DevOps Engineer"},
    {"id": 2, "name": "Priya", "role": "Software Engineer"},
    {"id": 3, "name": "Amit", "role": "Cloud Engineer"}
]


@app.route("/")
def home():
    return jsonify({
        "application": "DevOps Demo API",
        "version": "1.0",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/employees", methods=["GET"])
def get_employees():
    return jsonify(employees)


@app.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):

    for employee in employees:
        if employee["id"] == employee_id:
            return jsonify(employee)

    return jsonify({
        "error": "Employee not found"
    }), 404


@app.route("/employees", methods=["POST"])
def add_employee():

    data = request.get_json()

    employee = {
        "id": len(employees) + 1,
        "name": data["name"],
        "role": data["role"]
    }

    employees.append(employee)

    return jsonify(employee), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
