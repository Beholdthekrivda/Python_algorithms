# Сортировка вставками

import random

# создаем массив
l = []
for i in range(10):
    l.append(random.randint(0, 1000))  

for i in range(1, len(l)): # начинаем с 1 чтобы можно было считать предыдущий элемент 
    for j in range(i, 0, -1): # с каждой последущей итерацией наш диапазон поиска увеличивается на 1
    # это позволяет нам вставлять элемент в нужную позицию
        if l[j - 1] > l[j]:
            l[j], l[j - 1] = l[j - 1], l[j]

        else:
            break
print(l)
