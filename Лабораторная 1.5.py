import csv

flag = 0
nums = []
with open("books.csv") as csvfile:
    table = csv.reader(csvfile, delimiter=";")
    for row in list(table):
        while "#" in row[12]:
            row[12] = row[12].split(sep="#")
            nums = nums + row[12]
print(list(set(nums)))