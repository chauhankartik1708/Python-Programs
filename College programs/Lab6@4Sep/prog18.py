def removeRepeat(string):
    nonrepeated = []
    for i in string:
        if i not in nonrepeated:
            nonrepeated.append(i)

    nonrepeat = ''.join(nonrepeated)
    return nonrepeat

print(removeRepeat("Kaaaaaamleeeeesh"))