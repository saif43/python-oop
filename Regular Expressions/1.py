import re

pattern = r"pamspam"

if re.match(pattern, "spamspamspam"):
   print("Match")
else:
   print("No match")