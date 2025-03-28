import pickle

students = {}

with open("dictionary.pkl", "rb") as file:
    text = pickle.load(file)
    for key, value in text.items():
        students[key] = value

with open("file.txt", "w") as file:
    for name, point in students.items():
        file.write(f"{name} , {point}\n")