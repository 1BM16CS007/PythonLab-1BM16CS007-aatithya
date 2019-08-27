import random
import string
special_char = "!@%/()=?+.-"
pwlist = ([random.choice(special_char),
           random.choice(string.ascii_digits),
           random.choice(string.ascii_lowercase),
           random.choice(string.ascii_uppercase),
          ]  
         + [random.choice(string.ascii_lowercase
                          + string.ascii_uppercase
                          + special_char
                          + string.ascii_digits) for i in range(4)])
def is_valid(password):
    if len(password) < 8:
        return False
    if not any(c in password for c in special_char):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isupper() for c in password):
        return False
    return True
password_string = ''
random.shuffle(pwlist)
while not is_valid(password_string):
    password_string = ''.join(pwlist)
