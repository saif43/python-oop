import re

str = "My name is David. Hi David."
pattern = r"David"
print(re.sub(pattern, "Amy", str))
