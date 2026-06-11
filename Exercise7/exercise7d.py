"""
URL-encode characters—In URLs, we often replace special and nonprintable
characters with a % followed by the character’s ASCII value in hexadecimal. For
example, if a URL includes a space character (ASCII 32, aka 0x20), we replace
it with %20. Given a string, URL-encode any character that isn’t a letter or number.
For the purposes of this exercise, we’ll assume that all characters are in
ASCII (i.e., 1 byte long) and not multibyte UTF-8 characters. It might help to
know about the ord (http://mng.bz/EdnJ) and hex (http://mng.bz/nPxg)
functions.
"""
import string

def url_encode(url):

    no_encoding = string.ascii_letters + string.digits + '-._~/:'
    encoded_url = ''
    for char in url:
        if char in no_encoding:
            encoded_url += char
        else:
            encoded_url += f'%{str(hex(ord(char)))[2:]}'

    return encoded_url

print(url_encode("https://foo bar/foo~bar/foo&bar/foo*bar/foo%bar/foo-bar"))
