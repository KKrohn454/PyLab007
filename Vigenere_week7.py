from pydoc import plaintext
from sys import exit

def  vignere_head(alphabet):
    a = list(alphabet)
    a.insert(0, ' ')
    return a

def vigerene_sq(abc):
    alphabet = list(abc)
    sq_list = [vignere_head(abc)]
    for i in range(len(alphabet)):
        sq_list.append(list(alphabet[i]) + alphabet[i:] + alphabet[:i])
    return sq_list

def vigenere_print(alphabet):
    result = vigerene_sq(alphabet)
    for i, row in enumerate(result):
        if i == 1:
            print(f"|{'---|' * (len(alphabet) + 1)}")
        print(f"| {' | '.join(row)} |")

def letter_to_index(letter, alphabet):
    if not letter in alphabet:
        raise("Letter not in alphabet")
    return alphabet.find(letter)

def index_to_letter(index, alphabet):
    if 0 <= index < len(alphabet):
        return alphabet[index]
    return ''

def vigernere_index(key_letter, plaintext_letter, alphabet):
    ci = (letter_to_index(plaintext_letter, alphabet) + letter_to_index(key_letter, alphabet)) % len(alphabet)
    return index_to_letter(ci, alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    cipher_text = []
    key_len = len(key)
    for i, l in enumerate(plaintext):
        cipher_text.append(vigernere_index(key[i % key_len], l, alphabet))
    return ''.join(cipher_text)

def undo_vingenere_index(key_letter, cypher_letter, alphabet):
    pti = (letter_to_index(cypher_letter, alphabet) - letter_to_index(key_letter, alphabet)) % len(alphabet)
    return index_to_letter(pti, alphabet)

def decrypt_vigenere(key, cipher_text, alphabet):
    plaintext = []
    key_len = len(key)
    for i, l in enumerate(cipher_text):
        plaintext.append(undo_vingenere_index(key[i % key_len], l, alphabet))
    return ''.join(plaintext)

def enc_menu(key, alphabet, encrypted_list):
    plaintext = input("enter text to encrypt: ")
    encrypted_list.append(encrypt_vigenere(key, plaintext, alphabet))

def dec_menu(key, alphabet, encrypted_list):
    for cipher_text in encrypted_list:
        print(decrypt_vigenere(key, cipher_text, alphabet))

def dec_dump_menu(encrypted_list):
    for cipher_text in encrypted_list:
        print(cipher_text)

def main():
    key = 'DAVINCI'
    alphabet = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #message = 'the Eagle has landed'
    encrypted_list = []
    menu = [
        ['1. Encrypt', enc_menu, [key, alphabet, encrypted_list]],
        ['2. Decrypt', dec_menu, [key, alphabet, encrypted_list]],
        ['3. Dump Decrypt', dec_dump_menu, [encrypted_list]],
        ['4. Quit', exit, [0]]
    ]
    while True:
        print("-"*80)
        for menu_item in menu:
            print(menu_item[0])
        try:
            option = int(input('choose an option: '))
            if not (0 < option <= len(menu)):
                print("not an option")
            else:
                menu[option-1][1](*menu[option -1][2])
        except ValueError as ignoredError:
            print("input a menu number")
    #for _ in range(3):
       # encrypted_list.append(menu[0][1](*menu[0][2]))

    #menu[1][1](*menu[1][2])
    #menu[2][1](*menu[2][2])
    #menu[3][1](*menu[3][2])
main()