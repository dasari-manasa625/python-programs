import pandas as pd

# Load employee data
data = pd.read_csv(r"C:\Users\Hp\Desktop\python\employee_data.csv")

print("--- EMPLOYEE DATA ---")
print(data)

# Calculate average salary
average_salary = data["Salary"].mean()
print("\nAverage Salary:", average_salary)

# Count employees in each department
department_count = data["Department"].value_counts()
print("\nDepartment Count:")
print(department_count)

# Filter employees with salary above 55000
high_salary = data[data["Salary"] > 55000]

print("\nEmployees with Salary Above 55000:")
print(high_salary)

# Export filtered results
high_salary.to_csv("high_salary_employees.csv", index=False)

print("\nFiltered results exported successfully!")