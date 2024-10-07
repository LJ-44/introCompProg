# This code takes a user input password and replaces some characters to make it stronger, and adds "!" at the end

word = input()
password = ''

replacements = {"i":"1", "a":"@", "m":"M", "B":"8", "s":"$"}

for char in word:
    if char in replacements:
        password += replacements[char]
    else:
        password += char
password += "!!!"
print(password)
