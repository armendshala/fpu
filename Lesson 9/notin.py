import string

def notInserted():
    # type: () -> object
    characters = []
    for i in string.ascii_lowercase:
        for j in string.ascii_lowercase:
            characters.append(i + j)

    inserted = [str(x).strip() for x in open('Id.txt', 'rb')]
    notIn = set(characters) - set(inserted)
    return list(notIn)