numbers = [25, 10, 45, 5, 30, 15]

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

print("List:", numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)