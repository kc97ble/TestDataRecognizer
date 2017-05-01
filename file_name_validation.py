RESTRICTED_CHARS = "<>:\"/\\|?*"
APPROVED_SPECS = [
    (".in", ".out", "$"),
    ("in.", "out.", "^")
]


def is_valid(str):
    str = str.lower()
    for ch in str:
        if RESTRICTED_CHARS.__contains__(ch):
            return False
        if not (32 <= ord(ch) <= 126):
            return False
