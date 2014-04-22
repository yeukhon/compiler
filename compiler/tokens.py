# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import re

# Define a subset of Pascal token classes to be used by our compiler

TOKENS_CLASSES = [
    ("IDENTIFIER", "[a-zA-Z_][a-zA-Z0-9_]*"),
    ("EQUAL", "="),
    ("INTEGER", "\d+"),
    ("IGNORE", "[\s\t\n]+")
]
