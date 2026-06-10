"""
Consider an alternative version of Pig Latin—We don’t check to see whether the
first letter is a vowel, but, rather, we check to see whether the word contains two
different vowels. If it does, we don’t move the first letter to the end. Because the
word “wine” contains two different vowels (“i” and “e”), we’ll add “way” to the
end of it, giving us “wineway.” By contrast, the word “wind” contains only one
vowel, so we would move the first letter to the end and add “ay,” rendering it
“indway.” How would you check for two different vowels in the word? (Hint: sets
can come in handy here.)
"""

def pig_latin(word):

    vowels = set()
    for char in word:
        if char in 'aeiouAEIOU':
            vowels.add(char)

    if len(vowels) <= 1:
        return word[1:] + word[0] + 'ay'
    else:
        return word + 'way'

print(pig_latin("wine"))
print(pig_latin("wind"))
print(pig_latin("apple"))
print(pig_latin("bees"))
