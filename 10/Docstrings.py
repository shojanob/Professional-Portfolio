

# Return as an early exit
def format_name(f_name, l_name):
    """This is a docstring"""
    """Take a first and last name and 
    format it to return the title case version of the name. """
    if f_name == "" or l_name == "":
        return "Empty input"
    full_name = f_name.title() + " " + l_name.title()
    return f"{full_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))

"""Ctrl + / for multiple line comment"""
# ssdasad
# sdasda
# sadsadsdasad