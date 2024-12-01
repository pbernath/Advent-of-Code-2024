# Real input
file = open("real-input.txt", "r")
Lines = file.readlines()
file.close()


# Test input, expected outcome 31
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

similarity_score = 0

for num1 in list1:
    count = 0
    for num2 in list2:
        if num1 == num2:
            count += 1
    similarity_score += num1 * count

print("The similarity score is: ", similarity_score)
