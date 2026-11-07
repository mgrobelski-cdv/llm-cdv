import unittest

from chunker import chunk_text


class ChunkTextTests(unittest.TestCase):
    def test_chunks_words_up_to_limit(self):
        self.assertEqual(
            chunk_text("one two three four five", 2),
            ["one two", "three four", "five"],
        )

    def test_normalizes_whitespace_with_split_and_join(self):
        self.assertEqual(chunk_text("  one\t two\nthree  ", 2), ["one two", "three"])

    def test_preserves_word_order_spelling_and_punctuation(self):
        self.assertEqual(
            chunk_text("Hello, WORLD! isn't it?", 2),
            ["Hello, WORLD!", "isn't it?"],
        )

    def test_empty_text_returns_empty_list(self):
        self.assertEqual(chunk_text("", 3), [])
        self.assertEqual(chunk_text(" \t\n", 3), [])

    def test_nonpositive_limit_returns_empty_list(self):
        for limit in (0, -1, -5):
            with self.subTest(limit=limit):
                self.assertEqual(chunk_text("some words", limit), [])

    def test_one_word_limit(self):
        self.assertEqual(chunk_text("one two", 1), ["one", "two"])

    def test_limit_larger_than_word_count(self):
        self.assertEqual(chunk_text("one two", 5), ["one two"])


if __name__ == "__main__":
    unittest.main()
