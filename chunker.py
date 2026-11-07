"""Split text into consecutive chunks containing at most a set number of words."""


def chunk_text(text, max_words):
    """Return text as chunks of at most ``max_words`` whitespace-separated words.

    Words are taken from ``text.split()`` and joined with a single space in
    each chunk. Their order, spelling, and punctuation are preserved.
    """
    if max_words <= 0:
        raise ValueError("max_words must be greater than zero")

    words = text.split()
    return [
        " ".join(words[start : start + max_words])
        for start in range(0, len(words), max_words)
    ]
