max_number = 4000000

fib_1 = 0
fib_2 = 1

sum_of_evens = 0

while fib_2 < max_number:
    next_fib = fib_2 + fib_1
    fib_1 = fib_2
    fib_2 = next_fib

    if next_fib % 2 == 0:
        sum_of_evens += next_fib

print(sum_of_evens)