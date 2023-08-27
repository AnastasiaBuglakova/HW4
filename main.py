# # 1 Напишите функцию для транспонирования матрицы
# n = 5
# m = 3
# # исходная матрица
# my_matrix = [[i for i in range(j * n, j * n + n)] for j in range(m)]
# print(*my_matrix, sep='\n')
#
# # транспонируем ее
# transpon_matrix = [[my_matrix[i][j] for i in range(m)] for j in range(n)]
# print(*transpon_matrix, sep='\n')

# 2 Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.

# def key_dict(**kwargs):
#     new_dict = dict()
#     for key, value in kwargs.items():
#         if isinstance(value, list|set):
#             value = list(map(str, value))
#             value = ','.join(value)
#         elif isinstance(value, dict):
#             dict_in_str = ''
#             for key_, value_ in value.items():
#                 dict_in_str += f'{str(key_)}: {value_}, '
#             value = '{' + dict_in_str[:-2] + '}'
#         new_dict[value] = key
#     return new_dict
#
#
# print(key_dict(first='qwer', second=[2, 9], third=(4, 8, 9), fourth={4,5}, fifth={'r': 4, 'j':88}))

# 3 Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
# В ОТДЕЛЬНОМ ПРОЕКТЕ
