import itertools
import string

def brute_force_password_cracker(target_password):
    charset = string.ascii_lowercase
    
 
    for length in range(1, len(target_password) + 1):
        for guess in itertools.product(charset, repeat=length):
           
            guess_password = ''.join(guess)
            print(f'Trying: {guess_password}') 
            if guess_password == target_password:
                return f'Password cracked: {guess_password}'
    
    return 'Password not found'

target_password = 'safi' 
result = brute_force_password_cracker(target_password)
print(result)
