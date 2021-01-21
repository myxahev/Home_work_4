# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.


from sys import argv

script_name, first_param, second_param, third_param = argv

def simple_calc():
    x, y, z = int(first_param), int(second_param), int(third_param)
    return x * y + z

print(f'Размер заработной платы составил: {simple_calc() } $')

# python 4.1.py 40 150 5000
