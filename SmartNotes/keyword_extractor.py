def extract_keywords(text):
    words = text.split()
    keywords = []
    stop_words = ["is", "a", "the", "for", "to", "of", "in"]
    for word in words:
        word = word.strip(".,!?;:'\"()")
        lower_word = word.lower()
        if lower_word not in stop_words:
            keywords.append(lower_word)
    freq = {}
    for word in keywords:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1
    sorted_keywords = sorted(
        freq.items(),
        key=lambda item: item[1],
        reverse=True,
    )
    return sorted_keywords[:5]
