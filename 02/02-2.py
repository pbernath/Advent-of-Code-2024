# Real input
file = open("real-input.txt", "r")
Lines = file.readlines()
file.close()


# Test input, expected outcome 4
# file = open("test-input.txt", "r")
# Lines = file.readlines()
# file.close()

reports = []

for line in Lines:
    levels = line.split()
    
    int_levels = []
    
    for level in levels:
        int_levels.append(int(level))
    
    reports.append(int_levels)


safe_reports = 0

for report in reports:
    # print("Checking report: ", report)

    sublist = []
    sublist.append(report)

    for i in range(len(report)):
        new_sublist = report[:i] + report[i + 1:]
        sublist.append(new_sublist)

    safe = None

    for sub_report in sublist:
        # print("Checking sub report: ", sub_report)
        previous = None
        ascending = False
        descending = False
        for i, level in enumerate(sub_report):
            if previous is None:
                # print("First level")
                previous = level
                continue
            if abs(level - previous) > 3 or abs(level - previous) == 0:
                # print("Difference is not between 1 and 3, unsafe")
                safe = False
                break
            if ascending:
                if level < previous:
                    # print("Stopped ascending, unsafe")
                    safe = False
                    break
                else:
                    # print("Continuing to ascend")
                    previous = level
                    if i == len(sub_report) - 1:
                        safe = True
                        break
                    continue
            if descending:
                if level > previous:
                    # print("Stopped descending, unsafe")
                    safe = False
                    break
                else:
                    # print("Continuing to descend")
                    previous = level
                    if i == len(sub_report) - 1:
                        safe = True
                        break
                    continue
            if level > previous:
                # print("Marked as ascending")
                ascending = True
                previous = level
                continue
            if level < previous:
                # print("Marked as descending")
                descending = True
                previous = level
                continue
        if safe:
            # print("Safe report")
            safe_reports += 1
            break
        else:
            # print("Unsafe report")
            safe = None
            continue

print("Total number of safe reports:", safe_reports)


