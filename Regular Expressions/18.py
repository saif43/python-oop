import re

pattern = r"(\D+\d)"

match = re.match(pattern, "Hi 999!")

if match:
   print("Match 1")

match = re.match(pattern, "1, 23, 456!")
if match:
   print("Match 2")

match = re.match(pattern, " ! $?")
if match:
    print("Match 3")

# \d = digit
# \D = not digit

# \s = white space
# \S = not white space

# \w = word
# \W = not word


emailPattern = r'(\w)+ ([\w\d\.])+ @ ([\w])+ ([\w\d\.]) \.+([\w\d])+'

match = re.match(emailPattern, "saif.ahmed.anik.0@gmial.com")

if match:
    print(True)

