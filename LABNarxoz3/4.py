import csv
employees = {
    "103": "Hunold",
    "104": "Ernst",
    "105": "Austin",
    "106": "Pataballa",
    "107": "Lorentz",
    "120": "Weiss",
    "121": "Fripp",
    "122": "Kaufling",
    "123": "Vollman",
    "124": "Mourgos",
    "125": "Nayer",
    "126": "Mikkilineni",
    "127": "Landry",
    "128": "Markle",
    "129": "Bissot",
    "130": "Atkinson",
    "131": "Marlow",
    "132": "Olson"
}

def san(a, b = 2):
    print(a, b)
a = 3
san(a, 5)

# with open("employees.csv", "w") as file:
#     writer = csv.writer(file, delimiter=",")
#     writer.writerow(["employee_number", "employee_name"])
#     for key, value in employees.items():
#         writer.writerow([key, value])
