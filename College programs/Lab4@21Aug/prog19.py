name = "kaaaarrrrrrrrrtik"
nonrepeated = []

for i in name:
    if i not in nonrepeated:
        nonrepeated.append(i)

nonrepeat = ''.join(nonrepeated)
print(nonrepeat)