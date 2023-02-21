some_list = [1, 2, 3, 4, 5, 6]
# for ind in range(0, len(some_list)):
#     some_list[ind] = str(some_list[ind])
# print(some_list)

# new_list = list(map(str, some_list))
# print(new_list)

# new_list = list(filter(lambda x: x % 2 == 0, some_list))
# print(new_list)

# print(list(enumerate(some_list)))
# for ind, value in enumerate(some_list):
#     print(ind, value)

first_list = ['apple', 'orange', 'grape']
second_list = ["яблоко", "апельсин", "виноград"]
for eng, ru in zip(first_list, second_list):
    print(eng, ru)
