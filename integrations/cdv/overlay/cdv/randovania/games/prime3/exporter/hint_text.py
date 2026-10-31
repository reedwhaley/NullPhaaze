# Pure text helpers shared by client patching and server export metadata. Boundary names
# here: label.
"""Pure text helpers shared by client patching and server export metadata."""

def _safe(text):
    if not isinstance(text, str) or not text.strip() or len(text) > 240:
        raise ValueError('Invalid pickup scan item/player name')
    result = ''.join(c if c.isprintable() and c != '&' else ' ' for c in text).strip()
    if not result:
        raise ValueError('Empty pickup scan item/player name after markup removal')
    return result


def label(row):
    item = _safe(row['item_name'])
    if type(row.get('local')) is not bool:
        raise ValueError('Pickup scan ownership must be explicit')
    return f'Your {item}' if row['local'] else f"{_safe(row['recipient_name'])}'s {item}"

