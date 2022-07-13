import sys

# Get error messages according to what's missing
def get_message(has_min_len, has_letter, has_number, has_upper, has_lower):
    message = ''
    if not has_min_len:
        message += "Your password should be at least 10 characters\n"
    if not has_letter:
        message += "The password should contains at least one alphabetical characters\n"
    if not has_number:
        message += "Your password should contains at least one numerical characters\n"
    if not has_upper:
        message += "Your password should contains at least one capital letter\n"
    if not has_lower:
        message += "Your password should contains at least one lower letter"
    return message

# Validate the password, prints the success message or the error message and exit with code (0 -> success, 1 -> error)
def validate(p):
    code = 0
    has_min_len = False
    has_number = False
    has_letter = False
    has_upper = False
    has_lower = False
    if(len(p) >= 10):
        has_min_len = True
    for c in p:
        if c.isalpha():
            has_letter = True
        if c.isdigit():
            has_number = True
        if c.isupper():
            has_upper = True
        if c.islower():
            has_lower = True
        
    # If one of the condition is false so the password is incorrect
    if (not (has_min_len and has_letter and has_number and has_upper and has_lower)):
        code = 1
        message = get_message(has_min_len, has_letter, has_number, has_upper, has_lower)
        color = '\033[91m'
    else:
        code = 0
        message = 'The password is valid'
        color = '\033[92m'

    print(color + message + '\033[0m')
    sys.exit(code)

p = sys.argv[1]
validate(p)
