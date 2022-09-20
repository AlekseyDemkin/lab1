import csv

with open("books.csv") as csvfile:
    table = csv.reader(csvfile, delimiter=";")
    print(len(list(table)) - 1)
