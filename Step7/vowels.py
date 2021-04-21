string = input()
vowels = ['a','i','o','u','e']
total_vowels = 0
total_words = 0
for i in range(len(string)) :
    if string[i] != " ":
        if string[i].lower() in vowels:
            total_vowels+=1
    elif (i != 0 and i != len(string)-1) and string[i] == " ":
        total_words+=1
if total_words == 0:
    print(1,"word and vowels",total_vowels)
else:
    print(total_words+1," words and vowels",total_vowels)



 