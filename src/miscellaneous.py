def spellcheck(words, misspelled_word: str) -> str:
    """Given a misspelled word and a list of possible words, the function spellchecks the word and outputs the new one."""
    accuracy_indexes = [0] * len(words)
    for pos, word in enumerate(words):
        for x in range(min([len(word), len(misspelled_word)])):
            if word[x] == misspelled_word:
                accuracy_indexes[pos] += 1
    pos = accuracy_indexes.index(max(accuracy_indexes))
    return words[pos]