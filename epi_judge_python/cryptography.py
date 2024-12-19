


alphabet = [ascii for ascii in range(65, 91)]
rotation =3
def encrypt(text):
    return rotate(3,text)

def decrypt(text):
    return rotate(-3,text)

def rotate(rotation,text):
    result = []
    for char in text:
        key = (ord(char) - 65 + rotation) % len(alphabet)
        result.append(chr(alphabet[key]))
    return "".join(result)






assert "IUDQFR"== encrypt("FRANCO")
assert "IUDQC"== encrypt("FRANZ")
assert "FRANCO"== decrypt("IUDQFR")
assert "FRANZ"== decrypt("IUDQC")
