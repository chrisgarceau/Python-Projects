# import the necessary modules!
import secrets
import string

print('Password Generator')
print('------------------')

# input the length of password
length = int(input('\nEnter the length of password: '))                      

# define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = '~!?@$%?/^,.;:#&<>*(){}[]-+=|'

# combine the data
combined = lower + upper + num + symbols

# use secrets lib
password = ''.join(secrets.choice(combined) for i in range(length))

# print the password
print(password)
