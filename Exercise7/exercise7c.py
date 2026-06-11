"""
Remove author names—In academia, it’s common to remove the authors’ names
from a paper submitted for peer review. Given a string containing an article and
a separate list of strings containing authors’ names, replace all names in the
article with _ characters.
"""

def remove_names(filepath, names):
    with open(filepath, "r") as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        for author in names:
            line = line.replace(author, '___')
        new_lines.append(line)

    with open("./redacted_article.txt", "w") as new_file:
        new_file.writelines(new_lines)

path = "./journal_article.txt"
names = ["Andrew J. Martin", "Rebecca J. Collie"]
remove_names(path, names)
