import csv
from random import randint

flag = 0
with open("books.csv") as csvfile:
    table = csv.reader(csvfile, delimiter=";")
    f = open("resust.txt", "w")
    t = randint(1, 9389)
    i = "1"
    for row in list(table)[t:t+20]:
        f.write(i + ". " + row[3] + ". " + row[1] + " - " + row[6][:4] + "\n")
        i = int(i) + 1
        i = str(i)
