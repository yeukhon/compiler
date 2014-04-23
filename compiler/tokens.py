# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

RESERVED_KWS = [
    "program",
    "begin",
    "end",
    "var"
]

# Operators
tk_PLUS         = r"\+"
tk_SUB          = r"-"
tk_MUL          = r"\*"
tk_DIV          = r"/"
tk_GT           = r">"
tk_LT           = r"<"
tk_GE           = r">="
tk_LE           = r"<="
tk_EQUAL        = r"=="
tk_NOTEQUAL     = r"<>"
tk_ASSIGN       = r":=|="

# single-char operators/separators
tk_COLON        = r":"
tk_LPARN        = r"\("
tk_RPARN        = r"\)"
tk_LBRACK       = r"\["
tk_RBRACK       = r"\]"
tk_LBRACE       = r"\{"
tk_RBRACE       = r"\}"
tk_DOT          = r"\."
tk_COMMA        = r"\,"
tk_SEMI         = r"\;"

# Numbers literals
tk_INTEGER      = r"\d+"
tk_REAL         = r"\d+\.\d*"

# String literal
# Pascal string literal is enclosed in single quotes pair (less headache)
# See: http://pascal.comsci.us/tutorial/literal/string.html
# and: http://stackoverflow.com/a/2039820/230884
tk_STRING       = r'\'(\\.|[^"])*\''

# General identififer
tk_ID           = r"[a-zA-Z_][a-zA-Z0-9_]*"

# Whitespaces and newlines are to be ignored by the lexer (comments too)
tk_WSPACE       = r"[\s\t\n]+"

IGNORE = "WSPACE"

TOKEN_CLASSES = []

# For uniformity, we add a token class for reserved keywords.
# This is placed ahead of ID regex has order of precendence
# advantage so that we don't have to do branching in the lexer.
# Either way is fine.
TOKEN_CLASSES.append(("RESERVED", "|".join(RESERVED_KWS)))

for name, value in globals().items():
    if name.startswith("tk_"):
        TOKEN_CLASSES.append((name[3:], value))
