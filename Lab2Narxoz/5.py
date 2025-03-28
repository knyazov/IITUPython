import pickle

students = {}

with open("dictionary.pkl", "rb") as file:
    text = pickle.load(file)
    for key, value in text.items():
        students[key] = value
    sum = 0
    for name, salary in students.items():
        if (salary // 1000) % 2 == 0:
            sum += salary
    print(sum)