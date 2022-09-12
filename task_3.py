# Задача №32: Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def new_list(x):
    new_lst = []
    for i in x:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst 


_list = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {_list}")
n_list= new_list(_list)
print(f"Список из неповторяющихся элементов: {n_list}")
