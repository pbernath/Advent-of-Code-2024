import re

# Real input
file = open("real-input.txt", "r")
Lines = file.readlines()
file.close()


# Test input, expected outcome 48
# file = open("test-input-2.txt", "r")
# Lines = file.readlines()
# file.close()

pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

found_instructions = []

for i, line in enumerate(Lines):
    pattern_matches = re.findall(pattern, line)
    found_instructions.extend(pattern_matches)

results = 0
enabled = True

for instruction in found_instructions:
    match instruction:
        case "do()":
            enabled = True
        case "don't()":
            enabled = False
        case _ if enabled:
            instruction = instruction.replace("mul(", "")
            instruction = instruction.replace(")", "")
            instruction = instruction.split(",")
            results += int(instruction[0]) * int(instruction[1])

print("The result of adding up all the multiplications is:", results)