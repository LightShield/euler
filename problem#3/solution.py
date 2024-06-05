

target_number_to_find_prime_of = 600851475143

current_factor = 2
biggest_factor_found = current_factor


# while target_number_to_find_prime_of >= 0:
#     if current_factor >= target_number_to_find_prime_of:
#         break
#     if target_number_to_find_prime_of / current_factor == 0: 
#         target_number_to_find_prime_of /= current_factor
#         biggest_factor_found = current_factor
#         continue
#     current_factor+=1
#     print(f"current_factor = {current_factor}, biggest_factor_found = {biggest_factor_found}, target_number_to_find_prime_of = {target_number_to_find_prime_of}")

for i in range(1, target_number_to_find_prime_of, 1):
    if (target_number_to_find_prime_of / i).is_integer():
        print(i)
# print(biggest_factor_found)

