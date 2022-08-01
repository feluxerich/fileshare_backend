def to_alias(filename):
    alias = str()
    for char in filename:
        alias += f'{ord(char)}.'
    return alias[:-1]


def from_alias(alias):
    alias = alias.split('.')
    filename = str()
    for char in alias:
        filename += chr(int(char))
    return filename
