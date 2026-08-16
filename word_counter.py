file = open(r"C:\Users\Hp\Desktop\python\sample.txt", "r")

text = file.read()

words = len(text.split())
lines = len(text.splitlines())
characters = len(text)

print("Number of words:", words)
print("Number of lines:", lines)
print("Number of characters:", characters)

file.close()