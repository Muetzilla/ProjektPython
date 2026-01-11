def is_palindrome_number(n: int):
    s = str(n)
    return s == s[::-1]

def is_palindrome_string(s: str):
    return s == s[::-1]