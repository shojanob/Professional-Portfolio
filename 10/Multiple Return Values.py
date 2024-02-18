# Functions with Outputs

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Empty input"
    full_name = f_name.title() + " " + l_name.title()
    return f"{full_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))