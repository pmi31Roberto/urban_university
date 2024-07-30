def single_root_words(root_word, *other_words):
    same_words = []
    other_words_low = list(other_words)
    for i in range(len(other_words_low)):
        other_words_low[i] = other_words_low[i].lower()
    root_word_low = root_word.lower()

    for j in range(len(other_words_low)):
        if root_word_low in other_words_low[j] or other_words_low[j] in root_word_low:
            same_words.append(other_words[j])
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
