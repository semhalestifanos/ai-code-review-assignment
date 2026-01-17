import re

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def count_valid_emails(emails):
    try:
        iterator = iter(emails)
    except TypeError:
        raise TypeError("emails must be an iterable (e.g., list or tuple)")

    count = 0
    for e in iterator:
        if not isinstance(e, str):
            continue
        if _EMAIL_RE.match(e):
            count += 1
    return count