import StringIO
import unittest
import re

from lexer import Lexer, Token, join_regex
from tokens import TOKENS_CLASSES

class TestLexer(unittest.TestCase):
    def test_lexer_init(self):
        lexer = Lexer(TOKENS_CLASSES, file="example.input")
        self.assertEqual(lexer._file, "example.input")
        self.assertEqual(lexer._fstream is not None, True)
        self.assertEqual(lexer._lineno, 0)
        self.assertEqual(lexer._colno, 0)
        self.assertEqual(lexer._re,
            re.compile(join_regex(TOKENS_CLASSES)))

    def test_lexer_tokenizer_on_example_input(self):
        lexer = Lexer(TOKENS_CLASSES, file="example.input")
        tokens = []
        for token in lexer.tokenizer():
            tokens.append(token)

        expected_tks = [
            Token("IDENTIFIER", "a", 1, 0),
            Token("EQUAL", "=", 1, 2),
            Token("INTEGER", "1", 1, 4),
            Token("IDENTIFIER", "b", 2, 0),
            Token("EQUAL", "=", 2, 2),
            Token("INTEGER", "2", 2, 4)
        ]
        self.assertEqual(len(tokens), len(expected_tks))
        self.assertEqual(tokens, expected_tks)

if __name__ == "__main__":
    unittest.main()
