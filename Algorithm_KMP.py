# ЭТАП 1. Алгоритм нахождения максимальной длины суффикса

a = 'тарытар' # образец строки, которую будем искать в тексте или другой строчке

# создаем и заполняем массив в котором будут храниться длины суффиксов
# длина массива равна длине образца
p = [0] * len(a)
j = 0
i = 1

while i < len(a):
    # условие когда элементы образца и строки равные
    # по факту просто одновременно продвигаемся по элементам строки и образца
    if a[j] == a[i]:
        p[i] = j + 1
        i += 1
        j += 1
    else: # (if a[j] != a[i])
        # если каждый последующий элемент не равен первому, то длина суффикса 0
        if j == 0:
            p[i] = 0
            i += 1
        # это условие применяется тогда, когда было найдено совпадение i с элементом j
        # а элемент i+1 равен i, но при этом j увеличился на 1 и перестал быть равным i и i + 1
        # но так не должно быть и поэтмоу мы смещаем j на -1 
        # и получаем новое равенство
        else:
            j = p[j - 1]

# ЭТАП 2. Поиск образа в строке

a1 = 'тарытыры тарытары'
m = len(a)
n = len(a1)

i = 0
j = 0
while i < n:
    # если есть совпадения элементов в образце и строке, то увеличиваем индексы на 1
    if a1[i] == a[j]:
        i += 1
        j += 1
        if j == m:
            print('образ найден')
            break

    else:
        # честно, я не знаю как объяснить эту хуйню, тк чтобы понять нужно её визуализировать
        # ну она хотя бы работает :) 
        if j > 0:
            j = p[j - 1]
        else:
            i += 1
            if i == n:
                print('образ не найден')