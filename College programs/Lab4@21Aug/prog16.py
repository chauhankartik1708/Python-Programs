string = "kartik"
vowels = 0
consonants = 0
for i in string:
    if i in ('a','o','i','e','u','A','E','I','O','U'):
        vowels +=1
    else:
        consonants +=1
print(vowels)
print(consonants)