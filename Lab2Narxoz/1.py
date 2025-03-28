import pickle

students = {}

with open("dictionary.pkl", "rb") as file:
    text = pickle.load(file)
    for key, value in text.items():
        students[key] = value

    for name, point in students.items():
        print(f"{name} : {point}")

    print(students)