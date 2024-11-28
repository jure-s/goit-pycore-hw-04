def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid arguments. Use: add [username] [phone]"
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."