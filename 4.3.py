# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.
# Подсказка: используйте функцию range() и генератор.

list = [number for i, number in enumerate(range(20, 241)) if number % 20 == 0 or number % 21 == 0]
print(list)