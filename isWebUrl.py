import re, pyperclip

webUrlRegex = re.compile(r'(http://|https://|www.)(www\.)?([a-zA-Z0-9-_.]+)(\.[a-zA-Z0-9]{2,4})(\S+)')

text = str(pyperclip.paste())


mo = webUrlRegex.findall(text)

headers = []
domains = []
endings = []
directories = []
urls = []

for groups in mo:
    urls.append("".join(groups))
    headers.append(groups[0])
    domains.append(groups[2])
    endings.append(groups[3])
    directories.append(groups[4])


print("URLs found:")
for i in urls:
    print(i)

print("\n")
print("Headers:")
for i in headers:
    print(i)


print("\n")
print("Domains:")
for i in domains:
    print(i)

print("\n")
print("Endings:")
for i in endings:
    print(i)

print("\n")
print("Directories:")
for i in directories:
    print(i)


