import re, pyperclip

#Finds URLs beginning with www., http:// or https://
webUrlRegex = re.compile(r'(http://|https://|www.)(www\.)?([a-zA-Z0-9-_.]+)(\.[a-zA-Z0-9]{2,4})(\S+)')

#pastes from clipboard
text = str(pyperclip.paste())


mo = webUrlRegex.findall(text)

protocols = []
domains = []
tlds = []
paths = []
urls = []

#Splits the URL into 4 parts.
#http://www. | example | .org | /examples/examplepictures.html

for groups in mo:
    urls.append("".join(groups))
    protocols.append(groups[0])
    domains.append(groups[2])
    tlds.append(groups[3])
    paths.append(groups[4])


print("URLs found:")
for i in urls:
    print(i)

print("\n")
print("Protocols:")
for i in headers:
    print(i)


print("\n")
print("Domains:")
for i in domains:
    print(i)

print("\n")
print("Endings:")
for i in tlds:
    print(i)

print("\n")
print("Directories:")
for i in paths:
    print(i)


