numbers = [45, 12, 78, 23, 9, 56]

print("Original list:", numbers)

# Sort in ascending order
numbers.sort()
print("Sorted in ascending order:", numbers)

# Sort using lambda key
numbers.sort(key=lambda x: x)
print("Sorted using lambda:", numbers)