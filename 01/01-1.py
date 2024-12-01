# Real input
file = open("real-input.txt", "r")
Lines = file.readlines()
file.close()


# Test input, expected outcome 11
# file = open("test-input.txt", "r")
# Lines = file.readlines()
# file.close()

list1 = []
list2 = []

for line in Lines:
    num1, num2 = line.split()
    list1.append(int(num1))
    list2.append(int(num2))

list1.sort()
list2.sort()

# print(list1)
# print(list2)

total_distance = 0

for num1, num2 in zip(list1, list2):
    total_distance += abs(num1 - num2)

print("Total distance is:", total_distance)
