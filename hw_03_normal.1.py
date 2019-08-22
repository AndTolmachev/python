def fibonacci(n, m):
    fibonacci_list = [1, 1]
    if m > 2:
        for i in range(m - 2):
            fibonacci_list.append(fibonacci_list[i] + fibonacci_list[i+1])
    return fibonacci_list[n-1: m]


print(fibonacci(3,6))
