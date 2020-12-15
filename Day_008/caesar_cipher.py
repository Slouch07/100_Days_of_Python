import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbol = ['!', '@', '#', '$', '%', '^', '&', '*',
          '(', ')', '_', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8',
          '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# A function that will encrypt or decrypt a message by shifting the index of each character forward or backwards
# depending on the if you want to encode or decode the message.

def caesar(initial_message, shift_amount, cipher_direction):
    message_result = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    # Looping through each character in the message.
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            # Grabs the index of the letter from the alphabet and then shifts it by the given shift_amount and
            # then placing it in the message_result variable.
            cipher_letter = alphabet[index + shift_amount]
            message_result += cipher_letter
        elif char in symbol:
            index = symbol.index(char)
            # Ensures the message can still be encoded or decoded if the shift number given is larger than the list.
            if shift_amount > 11:
                shift_amount = shift_amount % 11
            cipher_letter = symbol[index + shift_amount]
            message_result += cipher_letter
        elif char in number:
            index = number.index(char)
            # Ensures the message can still be encoded or decoded if the shift number given is larger than the list.
            if shift_amount > 10:
                shift_amount = shift_amount % 10
            cipher_letter = number[index + shift_amount]
            message_result += cipher_letter
        else:
            # If the char is not found in any of the lists it is placed as is in the message_result variable.
            message_result += char
    print(f"The {cipher_direction}d text is: {message_result}")


# Import and print the logo from art.py
print(art.logo)

# A loop which keeps asking the user if they would like to continue using the cipher.
wants_restart = True
while wants_restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # Ensures the message can still be encoded or decoded if the shift number given is larger than the list.
    if shift > 26:
        shift = shift % 26

    caesar(initial_message=text, shift_amount=shift, cipher_direction=direction)

    restart = input(
        "Do you want to restart the cipher program? 'yes' or 'no': ").lower()
    if restart == "no":
        wants_restart = False
print("Goodbye")
