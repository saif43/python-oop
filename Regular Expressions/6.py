import re

pattern = r"^12.34$"

# The next two metacharacters are ^ and $.
# These match the start and end of a string, respectively.

if re.match(pattern, "12X34"):
    print('Match')
