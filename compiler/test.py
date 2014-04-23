import StringIO
import unittest
import re

import tokens
from lexer import Lexer, Token, join_regex

class TestLexer(unittest.TestCase):
    def test_lexer_init(self):
        lexer = Lexer(tokens.TOKEN_CLASSES, file="example.input")
        self.assertEqual(lexer._file, "example.input")
        self.assertEqual(lexer._fstream is not None, True)
        self.assertEqual(lexer._lineno, 0)
        self.assertEqual(lexer._colno, 0)
        self.assertEqual(lexer._pattern,
            join_regex(tokens.TOKEN_CLASSES))

    def test_lexer_tokenizer_on_example_input(self):
        lexer = Lexer(tokens.TOKEN_CLASSES, file="example.input")
        _tokens = []
        for token in lexer.tokenizer():
            _tokens.append(token)

        expected_tks = [
            Token("ID", "a", 1, 0),
            Token("ASSIGN", "=", 1, 2),
            Token("INTEGER", "1", 1, 4),
            Token("ID", "b", 2, 0),
            Token("ASSIGN", "=", 2, 2),
            Token("INTEGER", "2", 2, 4)
        ]
        self.assertEqual(len(_tokens), len(expected_tks))
        self.assertEqual(_tokens, expected_tks)

if __name__ == "__main__":
    unittest.main()
