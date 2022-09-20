import csv

count = 0
with open("books.csv") as csvfile:
    table = csv.reader(csvfile, delimiter=";")
    for row in list(table):
        if len(row[1]) > 30:
            count += 1
print(count)
