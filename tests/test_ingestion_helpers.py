import unittest

from ingestion.chunking import chunk_text
from ingestion.clean_text import clean_text


class IngestionHelpersTests(unittest.TestCase):
    def test_clean_text_strips_html_and_normalizes_whitespace(self):
        raw_html = "<div>Hello <b>world</b><br/> from   jobs</div>"

        cleaned = clean_text(raw_html)

        self.assertEqual(cleaned, "Hello world from jobs")

    def test_chunk_text_splits_long_text(self):
        long_text = "python data " * 120

        chunks = chunk_text(long_text)

        self.assertGreater(len(chunks), 1)
        self.assertTrue(all(chunk.strip() for chunk in chunks))


if __name__ == "__main__":
    unittest.main()
