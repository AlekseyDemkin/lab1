import csv

flag = 0
name = []
count = []
with open("books.csv") as csvfile:
    table = csv.reader(csvfile, delimiter=";")
    for row in list(table)[1:]:
        name.append(row[1])
        count.append(int(row[8]))
name_count = zip(count, name)  # соединяем списки, для совместной сортировки
name_count_sort = sorted(name_count,
                         key=lambda tup: tup[0])  # сортируем по первому элементу (в нашем случает по кол-ву выдач)
count_1 = [name_count[0] for name_count in name_count_sort]  # извлекаем отсортированные кол-ва выдач
name_1 = [name_count[1] for name_count in name_count_sort]  # извлекаем отсотированные по кол-ву выдач названия книг
print("Название книги - количество выдач")
for i in range(20):
    print(name_1[len(name_1) - i - 1], "-", count_1[len(count_1) - i - 1])
