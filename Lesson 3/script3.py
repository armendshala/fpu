import string

if __name__ == '__main__':

    for str1 in string.ascii_uppercase:
        for str2 in string.ascii_uppercase:
            character = '%s%s' % (str1,str2)
            print character