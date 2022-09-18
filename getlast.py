def getlast(s):
    """Finds the last word in a string of space delimited words"""
    # check input for content/spaces
    if not s or s.isspace():
        return "Invalid input"

    s = s.split(" ")
    last_word = s[-1]

    if last_word == "":
        return "Last word is a space"
    else:
        return last_word

input = "this is a sentence"
last = getlast(input)
print(last)

