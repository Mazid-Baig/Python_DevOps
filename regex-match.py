import re

text = "quick brown fox"
pattern = r"fox"

match = re.match(pattern, text)

if match:
    print("match found:", match.group())
else:
    print("match not found")


