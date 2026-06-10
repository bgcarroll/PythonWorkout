"""
Write a function that transposes a list of strings, in which each string contains
multiple words separated by whitespace. Specifically, it should perform in such a
way that if you were to pass the list ['abc def ghi', 'jkl mno pqr', 'stu vwx yz']
to the function, it would return ['abc jkl stu', 'def mno vwx', 'ghi pqr yz'].
"""

def transpose(list_of_strings):

    list_of_lists = [word.split() for word in list_of_strings]

    zipped = zip(*list_of_lists)
    transposed_lists = [
        ' '.join(list(item))
        for item in zipped
    ]

    return transposed_lists

print(transpose(['abc def ghi', 'jkl mno pqr', 'stu vwx yz']))
print(transpose(['abc def ghi', 'jkl mno pqr', 'stu vwx yz', 'foo bar roo', 'xabc xdef xghi']))
