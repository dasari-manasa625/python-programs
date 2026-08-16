import json

data = {
    "name": "Manasa",
    "age": 20,
    "course": "Python Programming"
}

with open(r"C:\Users\Hp\Desktop\python\student.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON file created successfully.")

with open(r"C:\Users\Hp\Desktop\python\student.json", "r") as file:
    data = json.load(file)

print("Data read from JSON file:")
print(data)