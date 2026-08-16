file1 = open(r"C:\Users\Hp\Desktop\python\file1.txt", "r")
file2 = open(r"C:\Users\Hp\Desktop\python\file2.txt", "r")

content1 = file1.read()
content2 = file2.read()

file1.close()
file2.close()

merged = open(r"C:\Users\Hp\Desktop\python\merged.txt", "w")

merged.write(content1)
merged.write("\n")
merged.write(content2)

merged.close()

print("Files merged successfully.")