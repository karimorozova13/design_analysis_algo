import time

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_dp(n):
    fib = [0] * (n + 1)
    
    # Базові випадки
    fib[0] = 0
    if n > 0:
        fib[1] = 1
    
    # Заповнення масиву
    for i in range(2, n + 1):
        fib[i] = fib[i-1] + fib[i-2]
    
    return fib[n]

def fibonacci_memo(n: int, memo: dict = None) -> int:
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# Порівняння ефективності

def time_function(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    print(f"{func.__name__}({n}) = {result}, Time: {end - start:.6f} seconds")

n = 35
time_function(fibonacci_recursive, n)
time_function(fibonacci_dp, n)
time_function(fibonacci_memo, n)

