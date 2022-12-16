import re
print("print IP:")
pattern = re.compile(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
def isValid(IP):
    if re.match(pattern, IP):
        print("Correct IP")
    else:
        print("Incorrect IP")
isValid(input())
