'''
Passwords must be at least 8 characters long (but they do not have an upper limit)

Passwords cannot contain the user’s username (i.e. if the username is ”My1stUsername” the password cannot be ”abcMy1stUsername” or ”My1stUsernameABC” because the username String can be found in the password String)

Passwords must be a mixture of uppercase letters (A-Z), lowercase letters (a-z), digits (0-9) and a select number of special characters (#, $, % and &). 
    The password must contain at least one of each of these types of characters in order to be valid.
'''

# Takes string and checks if it meets length requirement
# Returns length
# All usernames must be between 8 and 15 characters long
def get_length(s): 
    return len(s)

# Digits
#   0 - 48
#   9 - 57
# Uppercase
#   A - 65
#   Z - 90
# Lowercase
#   a - 97
#   z - 122

# valid_chars helper takes char and returns true if alphanumeric
def check_char(x):
    if x.isdigit() == True:
        return True
    elif x.isupper() == True:
        return True
    elif x.islower() == True:
        return True
    else:
        return False

# Takes string checks if all characters are valid
# Returns boolean
def valid_chars(s):
    length = len(s)
    for i in range(length):
        curr = s[i]
        if check_char(curr) == False:
            return False
    return True

# Takes string returns True if beginning and end are not digits
def check_ends(s):
    if s[0].isdigit() == True or s[-1].isdigit() == True:
        return False
    else:
        return True

# Takes string returns how many uppercase characters
def num_upper(s):
    length = len(s)
    tot = 0

    for i in range(length):
        char = s[i]
        if char.isupper() == True:
            tot += 1

    return tot

# Takes string returns how many lowercase characters
def num_lower(s):
    length = len(s)
    tot = 0

    for i in range(length):
        char = s[i]
        if char.islower() == True:
            tot += 1

    return tot

# Takes string returns how many digits
def num_digits(s):
    length = len(s)
    tot = 0

    for i in range(length):
        char = s[i]
        if char.isdigit() == True:
            tot += 1

    return tot

# Takes password string and finds number of special characters (# $ % &)
def num_special(p):
    length = len(p)
    tot = 0
    for i in range(length):
        char = p[i]
        if char == '#' or char == '$' or char == '%' or char == '&':
            tot += 1
    return tot

# Takes string determines if username is valid returns boolean
def is_valid(s):
    if get_length(s) >= 8 and get_length(s) <= 15 and valid_chars(s) == True and check_ends(s) == True and num_upper(s) > 0 and num_lower(s) > 0 and num_digits(s) > 0:
        return True
    else:
        return False

##################################################################################################################################################################################
##### Password section
##################################################################################################################################################################################

# Takes username and password returns True if username is found in password
def check_for_username(username, password):
    if username in password:
        return True
    else:
        return False

# Takes password, checks if valid and returns boolean
def valid_password(u, p):
    if get_length(p) >= 8 and check_for_username(u, p) == False and num_digits(p) > 0 and num_lower(p) > 0 and num_special(p) > 0:
        return True
    else:
        return False

def get_password(username):
    password = input('Enter a password: ')

    print('* Length of password: {}'.format(get_length(password)))
    print('* Username is part of password: {}'.format(check_for_username(username, password)))
    print('* # of uppercase characters: {}'.format(num_upper(password)))
    print('* # of lowercase characters: {}'.format(num_lower(password)))
    print('* # of digits: {}'.format(num_digits(password)))
    print('* # of special characters (#, $, %, &): {}'.format(num_special(password)))

    if valid_password(username, password) == False:
        print('Invalid password, please try again.\n\n')
        get_password(username)
    else:
        print('Password is valid!')

def get_username():
    username = input('Enter a username: ')

    print('* Length of username: {}'.format(get_length(username)))
    print('* All characters are alpha-numeric: {}'.format(valid_chars(username)))
    print('* First & last characters are NOT digits: {}'.format(check_ends(username)))
    print('* # of uppercase characters: {}'.format(num_upper(username)))
    print('* # of lowercase characters: {}'.format(num_lower(username)))
    print('* # of digits: {}'.format(num_digits(username)))

    if is_valid(username) == False:
        print('Username is invalid. Try again.\n\n')
        get_username()
    else:
        print('Username is valid!\n\n')
        get_password(username)

get_username()