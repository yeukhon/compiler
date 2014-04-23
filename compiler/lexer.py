# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import collections
import re
import tokens

INVALID_MSG = """\n
File "<{}>", line {}, starting at column {}
    {}
LexerError: invalid character in the input program.
"""

# Since tokens are mostly read-only we can use immutable named tuples
# instead of a full class.
Token = collections.namedtuple("Token", ["type", "value", "lineno", "colno"])

def join_regex(rules):
    """ Return a union of a list of regular expression
    in a named group form. Each item in the list
    is a tuple of (name, regex). """

    return "|".join("(?P<%s>%s)" % rule for rule in rules)

class Lexer(object):
    """ A Yo-mama Yoda style Lexer. The job of a lexer (aka scanner)
    is to consume a text program, read one character at a time,
    and match as many characters as possible for one specific regular
    expression and return that token class. """

    def __init__(self, rules, file=None, fstream=None):
        if file or fstream:
            if file and fstream and file != fstream.name:
                raise Exception("fstream and file name don't match.")
            elif file and not fstream:
                self._fstream = open(file, "r")
                self._file = file
            elif not file and fstream:
                self._fstream = fstream
                self._file = fstream.name

            # Initialize both to zero. For column we will use zero-index.
            # For the line number, self.tokenizer() will increment line
            # number to start at 1 at the beginning.
            self._lineno = 0
            self._colno = 0

            self._rules = rules
            self._re = re.compile(join_regex(rules))

    def tokenizer(self):
        """ Returns a generator object which yields a token class
        as the lexer continues to read in characters and match
        one of the regular expressions. """

        token = None
        for line in self._fstream:
            self._lineno += 1
            self._colno = 0
            while self._colno < len(line):
                # The match, if any, should be found as long as possible
                # starting from self._colno position in the current line
                match = self._re.match(line, self._colno)
                if match:
                    type = match.lastgroup
                    if type != tokens.IGNORE:
                        token = Token(type, match.group(),
                                      self._lineno, self._colno)
                        yield token
                    self._colno = match.end()+1
                else:
                    # Close file descriptor
                    self._fstream.close()
                    raise Exception(INVALID_MSG.format(self._file,
                        self._lineno, self._colno, line))
        # Close the file descriptor
        self._fstream.close()
