import statistics

def word_stats(words):
    lengths = [len(word) for word in words]
    return min(lengths), max(lengths), round(statistics.mean(lengths), 2)


print(word_stats(['foo', 'baroo', 'foobaroo', 'python', 'statistics', 'of']))
