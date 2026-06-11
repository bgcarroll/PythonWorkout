"""
This exercise is meant to help you practice thinking in this way. Here, you’ll implement
a translator from English into another secret children’s language, Ubbi Dubbi
(http://mng.bz/90zl). (This was popularized on the wonderful American children’s
program Zoom, which was on television when I was growing up.) The rules of Ubbi
Dubbi are even simpler than those of Pig Latin, although programming a translator is
more complex and requires a bit more thinking.
In Ubbi Dubbi, every vowel (a, e, i, o, or u) is prefaced with ub. Thus milk becomes
mubilk (m-ub-ilk) and program becomes prubogrubam (prub-ogrub-am). In theory, you
only put an ub before every vowel sound, rather than before each vowel. Given that this
is a book about Python and not linguistics, I hope that you’ll forgive this slight difference
in definition.
Ubbi Dubbi is enormously fun to speak, and it’s somewhat magical if and when you
can begin to understand someone else speaking it. Even if you don’t understand it,
Ubbi Dubbi sounds extremely funny. See some YouTube videos on the subject, such as
http://mng.bz/aRMY, if you need convincing.
For this exercise, you’ll write a function (called ubbi_dubbi) that takes a single
word (string) as an argument. It returns a string, the word’s translation into Ubbi
Dubbi. So, if the function is called with octopus, the function will return the string
uboctubopubus. And if the user passes the argument elephant, you’ll output
ubelubephubant.
As with the original Pig Latin translator, you can ignore capital letters, punctuation,
and corner cases, such as multiple vowels combining to create a new sound.
When you do have two vowels next to one another, preface each of them with ub.
Thus, soap will become suboubap, despite the fact that oa combines to a single vowel
sound.
Much like the Pig Latin sentence exercise, this exercise brings to the forefront the
various ways we often need to scan through strings for particular patterns or translate
from one Python data structure or pattern to another and how iterations can play a
central role in doing so.
"""

def ubbi_dubbi(word):

    my_new_word = ''.join([
        'ub'+ letter if letter in 'aeiouAEIOU' else letter
        for letter in word
    ])

    return my_new_word

print(ubbi_dubbi("cat"))
print(ubbi_dubbi("soap"))
print(ubbi_dubbi("octopus"))
print(ubbi_dubbi("elephant"))
