"""
Given the string 'Tom Dick Harry', break it into individual words and then sort
those words alphabetically. Once they’re sorted, print them with commas (,)
between the names.
"""

def breakup(a_string):
    print(','.join(sorted(str.split(a_string))))

breakup("Tom Dick Harry")
