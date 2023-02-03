# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.

n = int(input('Введите количество арбузов: '))
min = 30000
max = 0
for _ in range(n):
    weight = int(input())
    if weight > max:
        max = weight
    if weight < min:
        min = weight
print(f'Самый тяжелый арбуз: {max} кг, самый легкий арбуз: {min} кг')

