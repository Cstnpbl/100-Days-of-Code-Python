alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

yes=True

def caesar(code_or_decode,original_text,shift_amount):
    cypher_text = ""

    if code_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
                cypher_text += letter
        else:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= 26
                cypher_text += alphabet[shifted_position]

    print(cypher_text)

while yes:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction,text,shift)
    yes=input("Type 'yes' if you want to go again. Otherwise, type 'no'\n").lower()
    if yes=="no":
        yes=False
    else:
        yes=True





