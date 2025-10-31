# return = statement used to end a function
#           and send a result back to the caller

def create_name(first_name, last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return f"{first_name} {last_name}"

full_name = create_name("aNSH", "singH")
print(full_name)