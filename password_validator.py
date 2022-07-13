import sys

def validate(p):
    code = 0
    message = 'The password is valid'
    if(len(p) <= 10):
        message = "Your password should be at least 10 characters"
        code = 1
    if p.isalpha():
        message = "Your password should contains alphabetical characters"
        code = 1
    if p.isdigit():
        message = "Your password should contains numerical characters"
        code = 1
    if p.isupper():
        message = "Your password should contains at least one capital letter"
        code = 1
    if p.islower():
        message = "Your password should contains at least one lower letter"
        code = 1
    # Color code RED if there is an error
    if code == 1:
        color = '\033[91m'
    # Color code GREEN if the password fill the requirement
    else:
        color = '\033[92m'
    print(color + message + '\033[0m')
    sys.exit(code)

p = sys.argv[1]
validate(p)
