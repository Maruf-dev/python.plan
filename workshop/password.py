def good_length(s):
    if len(s) > 8 and len(s) <= 64 :
        return True
    else:
        return False
# This should print False, because it's under eight characters.
print(good_length("2short"))

# This should print True, since it's between eight and 64 characters long:
print(good_length("nice password, yo"))

# This should print False, since it's over 64 characters long:
print(good_length("This is really much too long for a password. I mean, it's really secure, but I don't want to type this much every time I log in, okay?"))
"""2chi versiyasi 
def good_length(s):
    return len(s) > 8 and len(s) < 64"""