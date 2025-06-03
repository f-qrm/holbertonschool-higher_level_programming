def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as filename:
        return(filename.write(text))
