def open_file():
    try:
        with open ("ejemplo.txt", "r") as archive:
            content = archive.read()
        return print(content)
    except FileNotFoundError:
        return print("The archive in the path doesn't exist")



hello = open_file()
