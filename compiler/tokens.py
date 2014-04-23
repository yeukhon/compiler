# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import collections

TK = collections.namedtuple("TK", ["id", "name", "regex"])

IGNORE = TK(0, "IGNORE", "[\s\t\n]+")
ID = TK(1, "IDENTIFIER", "[a-zA-Z_][a-zA-Z0-9_]*")
EQUAL = TK(2, "EQUAL", "=")
INTEGER = TK(3, "INTEGER", "\d+")

TOKEN_CLASSES = []
for name, value in globals().items():
    if isinstance(value, TK):
        TOKEN_CLASSES.append((value.name, value.regex))
