from functools import lru_cache

@lru_cache(maxsize=10)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

@lru_cache(maxsize=None, typed=False)
def square_false(x):
    print(f"Computing square for {x}")
    return x * x

@lru_cache(maxsize=None, typed=True)
def square_true(x):
    print(f"Computing square for {x}")
    return x * x

print(square_false(3))  # Output: Computing square for 3
print(square_false(3.0))  # Output: 9 (очікуємо без повторного обчислення)

print(square_true(3))  # Output: Computing square for 3
print(square_true(3.0))  # Output: Computing square for 3.0

print(fib(10))
print(fib(15))
print(fib(20))

# Виводимо статистику кешу
print(fib.cache_info())
