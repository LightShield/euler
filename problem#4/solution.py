# number possible number from a product of 2 3-digit numbers is 999*999 = 998001

def is_palindorme(number):
    number_as_string = str(number)
    for i in range(0, int(len(number_as_string)/2)):
        if number_as_string[i] !=  number_as_string[len(number_as_string) - 1 -i]:
            return False
    return True

# find all palindromes with the relevant amount of digits
def get_all_relevant_palindromes():
    palindromes = []
    for i in range(999*999, 100000, -1):
        if(is_palindorme(i)):
            palindromes.append(i)
    return palindromes
    
palindromes = get_all_relevant_palindromes()

# for the relevant palindrom, find the largest number that divides it to an int, and try that
for palindorm in palindromes:
    print(f"Attempting palindrom: {palindorm}")
    for i in range(999,100,-1):
        if (palindorm/i).is_integer() and (palindorm/i) < 1000:
            print(f'palindrome = {palindorm} = {i} * {palindorm/i}')
            exit(0) 
