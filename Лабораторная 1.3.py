import csv

flag = 0
data = input("Autor: ")
with open("books.csv") as csvfile:
    table = csv.reader(csvfile, delimiter=";")
    for row in list(table):
        lower_case = row[3].lower()
        index = lower_case.find(data.lower())
        if index != (-1):
            print(row)
            flag = 1
    if flag == 0:
        print("nothing find")
