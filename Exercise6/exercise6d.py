"""
Read through an Apache logfile. If there is a 404 error—you can just search for
' 404 ', if you want—display the IP address, which should be the first element.
If you don’t have such a logfile handy, you can get mini-access-log.txt in the
zipfile at https://files.lerner.co.il/exercise-files.zip.
"""

def display_404(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    for line in lines:
        if ' 404 ' in line:
            print(line[:line.index(' - - ')])

display_404('./exercise-files/mini-access-log.txt')
