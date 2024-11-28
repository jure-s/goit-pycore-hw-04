def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid arguments. Use: phone [username]"
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return f"Contact {name} not found."