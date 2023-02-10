# Напишите программ, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Кол-во повторов добавляется к символам с помощью постфикса формата _n

string = 'd g h t r g r h t j h b v f d s d f'
print(string)
my_list = string.split()
my_dict = {}
new_list = []
for letter in my_list:
    my_dict[letter] = my_dict.get(letter, 0) + 1
    if my_dict.get(letter) > 1:
        new_list.append(letter + '_' + str(my_dict.get(letter)))
    else:
        new_list.append(letter)
print(' '.join(new_list))
