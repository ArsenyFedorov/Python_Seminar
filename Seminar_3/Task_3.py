# Напишите программу для печати всех уникальных значений в словаре.
my_list = [{"V": "S001"},
           {"V": "S002"},
           {"VI": "S001"},
           {"VI": "S005"},
           {"VII": "S005"},
           {"V": "S009"},
           {"VIII": "S007"}]
print(my_list)
my_dict = list()
for i in range(len(my_list)):
    my_dict.append(my_list[i].values())
print(set(my_dict))
