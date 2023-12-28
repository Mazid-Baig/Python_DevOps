import re

text = "quick brown fox"
pattern = r"fox"

replacement = "bear"

replace = re.sub(pattern, replacement, text)


print(replace)
