import re

text = "the quick brown fox"
pattern = r'fox'

search = re.search(pattern, text)

if search:
    print("pattern found:", search.group())

else:
    print("not found")