import pickle

students = {}

with open("dictionary.pkl", "rb") as file:
    text = pickle.load(file)
    for key, value in text.items():
        students[key] = value
    max, name = 0, ""
    for key, salary in students.items():
        if salary > max:
            max = salary
            name = key
    print(name, max)