import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
temperature = [30, 32, 31, 35, 33]

plt.plot(days, temperature, marker="o")

plt.title("Temperature Over 5 Days")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")

plt.grid(True)
plt.show()