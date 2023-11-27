import re
print("print IP:")
pattern = re.compile(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")
def isValid(IP):
    if re.match(pattern, IP):
        print("Correct IP")
    else:
        print("Incorrect IP")
isValid(input())
