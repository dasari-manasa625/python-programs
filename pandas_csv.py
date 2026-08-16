import pandas as pd

data = pd.read_csv(r"C:\Users\Hp\Desktop\python\students.csv")

print("Student Data:")
print(data)

print("\nAverage Marks:", data["Marks"].mean())
print("Highest Marks:", data["Marks"].max())
print("Lowest Marks:", data["Marks"].min())