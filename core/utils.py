from sqids import Sqids

sqids = Sqids(min_length=6)

def encode_id(num: int) -> str:
    """Encodes an integer to a base62 string."""
    return sqids.encode([num])

def decode_url(encoded_str: str) -> int:
    """Decodes a base62 string back to an integer."""
    decoded = sqids.decode(encoded_str)
    if not decoded:
        raise ValueError("Invalid short code")
    return decoded[0]    