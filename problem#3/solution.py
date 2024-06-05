

target_number_to_find_prime_of = 600851475143

i = 2
while i <= target_number_to_find_prime_of:
    if (target_number_to_find_prime_of / i).is_integer():
        print(f'{target_number_to_find_prime_of} = {i} * {target_number_to_find_prime_of / i}')
        target_number_to_find_prime_of /= i
        
    else:
        i += 1

print(f'final answer : {i}')
