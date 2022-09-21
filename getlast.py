import sys


def getlast(s):
    """Finds the last word in a string of space delimited words"""
    # check input for content/spaces
    if not s or s.isspace():
        return "Invalid input"

    # split string on spaces in to list, access last element
    s = s.split(" ")
    last_word = s[-1]

    # check if last element is valid
    if last_word == "":
        return "Last word is a space"
    else:
        return last_word


if __name__ == "__main__":
    """Allows command line arg parsing"""

    # use format would be: python3 ./getlast.py "this is a sentence"
    res = getlast(sys.argv[1])
    print(res)
