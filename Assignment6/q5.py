#Write a Python program to understand the use of and variables & declared in a function.
# declare global variable
message = 'Hello'
# outside function 
def outer():
    message = 'local'

    # nested function  
    def inner():

        # declare nonlocal variable
        nonlocal message
        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()