def to_alias(filename):
    alias = str()
    for char in filename:
        alias += f'{ord(char)}.'
    return alias


def from_alias(alias):
    alias = (alias.split('..'))[0].split('.')
    filename = str()
    for char in alias:
        filename += chr(int(char))
    return filename


def get_filesize(alias):
    return (alias.split('..'))[1]
