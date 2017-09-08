import re

emailRegex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4})')

no = emailRegex.search("crag@gmail.com is an email")

print(no.group())

