def is_palindrome(text):
    text= text.lower()
    rev= ""

    for char in text:
        rev= char + rev
    if text == rev:
        return True
    else:
        return False