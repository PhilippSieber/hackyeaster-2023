from random import randint

replacements = {
    ' ': [' '],
    '{': ['{'],
    '}': ['}'],
    'a': ['🥔', '🍠'],
    'b': ['🍌'],
    'c': ['🥐'],
    'd': ['🍑', '🍈'],
    'e': ['🍒', '🫐', '🍇'],
    'f': ['🌽'],
    'g': ['🍐'],
    'h': ['🍉'],
    'i': ['🍍', '🥭'],
    'j': ['🥨'],
    'k': ['🥒'],
    'l': ['🌶', '🫑'],
    'm': ['🍅'],
    'n': ['🍓'],
    'o': ['🥝'],
    'p': ['🥕','🥦'],
    'q': ['🥯'],
    'r': ['🥥'],
    's': ['🍊', '🍋'],
    't': ['🍏', '🍎'],
    'u': ['🥖'],
    'v': ['🥬'],
    'w': ['🥑'],
    'x': ['🍆'],
    'y': ['🧅', '🧄'],
    'z': ['🫒']
}

def encrypt(plain):
    cipher = ''
    for i in plain:
        chars = replacements[i]
        l = len(chars)
        cipher += replacements[i][randint(0,l-1)]
    return cipher

def decrypt(cipher):
    plain = ''
    for i in cipher:
        for j in replacements:
            if i in replacements[j]:
                plain += j
    return plain

# encrypt plain text
plain = 'possibly you have heard about ciphers which map single plaintext letters to more than one ciphertext letters these are called homophonic ciphers the solution is hypervitaminosis'
cipher = encrypt(plain)
print(cipher)

# check
plain2 = decrypt(cipher)
assert (plain == plain2)


