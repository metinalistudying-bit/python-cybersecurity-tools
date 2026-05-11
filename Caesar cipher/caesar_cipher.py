import logo

print(logo.cipher_logo)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z',
            'a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_word = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_word += alphabet[shifted_position]
        else:
            output_word += letter
    print(f"Here is the {encode_or_decode}d result: {output_word}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Insert message: ")
    shift = int(input("Insert shift: "))
    caesar(text, shift, direction)
    restart = input("Type 'Y' to go again. Otherwise type 'N'\n").lower()
    if restart == "n":
        should_continue = False