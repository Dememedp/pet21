def replace_symbols(str):
    newstr = ""
    for letter in str:
        if letter == "'":
            newstr += "\""
        elif letter == "\"":
            newstr += "'"
        else:
            newstr +=letter
    return newstr

str = input("input a string\n")
print(replace_symbols(str))