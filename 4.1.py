from sys import argv

script_name, first_param, second_param, third_param = argv

def simple_calc():
    x = int(first_param)
    y = int(second_param)
    z = third_param
    if z == '30%':
        return (x * y) + (0.3 * (x * y))
    elif z == '50%':
        return (x * y) + (0.5 * (x * y))
    else:
        return x * y
print(f'Размер заработной платы составил: {simple_calc() } $')

# python 4.1.py 40 150 30%
# python 4.1.py 40 150 50%