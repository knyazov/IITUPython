import pickle

students = {}

with open("dictionary.pkl", "rb") as file:
    text = pickle.load(file)
    for key, value in text.items():
        students[key] = value
    min = 9999999
    min_name = ""
    for name, salary in students.items():
        if len(name) < min:
            min = len(name)
            min_name = name
    print(min_name)