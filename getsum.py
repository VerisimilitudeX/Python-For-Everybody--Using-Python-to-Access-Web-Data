import re

file = open("regex_sum_1582648.txt", "rt")
count = 0


for line in file:
    nums = re.findall("[0-9]+", line)
    if len(nums) != 0:
        for num in nums:
            count += int(num)

print(count)