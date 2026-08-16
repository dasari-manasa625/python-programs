file = open(r"C:\Users\Hp\Desktop\python\sample.txt", "r")

lines = file.readlines()

print("Total number of lines:", len(lines))

file.close()