import pickle

students = {}

with open("dictionary.pkl", "rb") as file:
    text = pickle.load(file)
    for key, value in text.items():
        students[key] = value
    counter = 0
    for key, salary in students.items():
        if salary > 10000:
            counter += 1
    print(counter)