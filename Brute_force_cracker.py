import itertools
import string

def brute_force_password_cracker(target_password):
    # Define the character set to use (lowercase letters)
    charset = string.ascii_lowercase
    
    # Start trying combinations of increasing lengths
    for length in range(1, len(target_password) + 1):
        for guess in itertools.product(charset, repeat=length):
            # Join the tuple to form a string
            guess_password = ''.join(guess)
            print(f'Trying: {guess_password}')  # Optional: Print the guess
            if guess_password == target_password:
                return f'Password cracked: {guess_password}'
    
    return 'Password not found'

# Example usage
target_password = 'abc'  # Change this to the password you want to crack
result = brute_force_password_cracker(target_password)
print(result)
