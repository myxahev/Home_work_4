from sys import argv

script_name, first_param, second_param, third_param = argv

def simple_calc():
    x = int(first_param)
    y = int(second_param)
    z = int(third_param)
    return (x * y) + (z * (x * y))



print(f'Размер заработной платы составил: {simple_calc() } $')

# python 4.1.py 40 150 30%
# python 4.1.py 40 150 50%