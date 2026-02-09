# Coding Username and Password Verification 
from pyscript import display, document #type:ignore 

def account_authenticator(e):
    # Clear previous output 
    document.getElementById('output').innerHTML = ''
    
    # Get values
    uname = document.getElementById('input1').value
    pword = document.getElementById('input2').value

    # Nested Ifelse

    if len(uname) >= 7: 
        display(f"Your username, {uname}, has been authenticated!", target ="output")  # If username passes all requirements this will display 
    else: 
        display(f'Your username must have seven characters or more', target='output')  # Checking for username length

# Checking for letetrs within the password
    if len(pword) >= 10:
        if not pword.isalpha():
            if pword.isdigit():
                display(f"Your password must contain letters and numbers.", target='output')
            # If all passwords checks pass, this will display
            else:
                display(f'Your password has been authenticated!', target='output')
        # Checking for numbers within password
        elif pword.isalpha():
            display(f'Your password must contain letters and numbers.', target='output')
    # Checking for password length
    elif not len(pword) >= 10:
        display(f'Your password must have a minimum of 10 characaters', target="output")
   
    # Checking if username and password passses all checks 

    has_letter = False
    has_number = False
    
    for char in pword:
        if char.isalpha():
            has_letter = True
        if char.isdigit():
            has_number = True
            
   
    if len(uname) >= 7 and len(pword) >= 10 and has_letter == True and has_number == True:
        display(f'Username and Password passes all required checks! Account has been authenticated.', target='output')
    else:
        display(f'Username or Password does not pass all required checks.', target='output')

    