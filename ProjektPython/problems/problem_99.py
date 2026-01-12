# Problem 99
# Comparing pairs of base and exponent from a file to determine which pair yields the greatest numerical value
# The file "base_exp.txt" contains one thousand lines with a base/exponent pair on each line.
# Determine which line number has the greatest numerical value.
import numpy as np

data = []

with open("../additional_files/0099_base_exp.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        a, b = line.split(",")
        data.append((int(a), int(b)))

log_data = []
for i in range(len(data)):
    a, b = data[i]
    log_data.append(b * np.log(a))
max_index = np.argmax(log_data)
print(max_index + 1)
print(data[max_index])
