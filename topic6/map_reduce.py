numbers = [1, 2, 3, 4, 5]

for i in map(lambda x: x ** 2, numbers):
    print(i)

squared_nums = list(map(lambda x: x ** 2, numbers))
print(squared_nums)

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = map(lambda x, y: x + y, nums1, nums2)

print(list(sum_nums))

nums = [1, 2, 3, 4, 5]
squared_nums1 = [x * x for x in nums]
print(squared_nums1)

from functools import reduce

# Приклад 1: Обчислення суми всіх елементів списку
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)  # Виведе 15 (1 + 2 + 3 + 4 + 5 = 15)

# Приклад 2: Об'єднання рядка зі списку рядків
words = ["Hello", "World", "Python"]
sentence = reduce(lambda x, y: x + " " + y, words)
print(sentence)  # Виведе "Hello World Python"

# Приклад 3: Знаходження максимального числа у списку
numbers3 = [10, 4, 25, 7, 31]
max_num = reduce(lambda x, y: x if x > y else y, numbers3)
print(max_num)  # Виведе 31 (максимальне число у списку)

result = reduce((lambda x, y: x * y), [1, 2, 3, 4], 3)

print(result)

