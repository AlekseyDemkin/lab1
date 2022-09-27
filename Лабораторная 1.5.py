import csv

flag = 0
nums = []
with open("books.csv") as csvfile:
    table = csv.reader(csvfile, delimiter=";")
    for row in list(table):
        while "#" in row[12]:
            row[12] = row[12].split(sep="#")
            nums = nums + row[12]
    for i in range(len(nums)):
        if nums[i][0] == " ":
            nums[i] = nums[i][1:]
        if nums[i][-1] == " ":
            nums[i] = nums[i][:-1]
nums = list(set(nums))
for i in range(len(nums)):
    print(i+1, nums[i])
