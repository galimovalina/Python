# Напишите программу для печати всех уникальных значений в словаре. \

list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
set_1 = set()
for i in list_1:
    print(i)
    for j in i:
        print(j)
        set_1.add(i[j])
print(set_1)