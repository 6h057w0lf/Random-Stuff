# Pig Latin Transalator
# this litte program ask for a sintance and print thesintance back in pig latin.


# get sintance from user

original = input("Please enter a sentence: ").strip().lower()
                 
# split sinteance in to words

words= original.split()
                 
                 
# lop words and convert to pig latin

new_words = []

for word in words:
    if word[0] in "aiou":
       new_word = word + "yay"
       new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aiou":
                vowel_pos = vowel_pos + 1
            else:
                break
            cons = word[:vowel_pos]
            the_rest = word[vowel_pos:]
            new_word = the_rest + cons + "ay"
            new_words.append(new_word)
                 

# stck words back togather

output = " ".join(new_words) 

# output the file string

print(output)


