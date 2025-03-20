import json

with open("employees.json", "r") as file:
    employees = {}
    out = json.load(file)
    for employee_number in out:
        employee_name = out[employee_number]
        employees[employee_number] = employee_name
    print(employees)
    for key in employees:
        print(key, ":", employees[key])