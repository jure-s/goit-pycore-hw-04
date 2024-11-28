def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid arguments. Use: change [username] [phone]"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact {name} updated."
    else:
        return f"Contact {name} not found."