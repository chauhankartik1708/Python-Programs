string = "kartik"
vowels = 0
consonants = 0
for i in string:
    if i in ('a','o','i','e','u'):
        vowels +=1
    else:
        consonants +=1
print(vowels)
print(consonants)