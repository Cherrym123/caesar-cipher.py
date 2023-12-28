# # Step - 1
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def encrypt(text, shift):
#     encrypted_text=""
#     for letter in text:
#         index=alphabet.index(letter)
#         after_shift=index+shift
#         encrypted_text += alphabet[after_shift]
#     print(f"The encoded text is {encrypted_text}")

# def decrypt(text, shift):
#     decrypted_text=""
#     for letter in text:
#         index=alphabet.index(letter)
#         after_shift=index-shift
#         decrypted_text += alphabet[after_shift]
#     print(f"The decoded text is {decrypted_text}")

# if direction == "encode":
#     encrypt(text,shift)
# elif direction == "decode":
#     decrypt(text,shift)
# else:
#     print("please choose correct direction..!")

# Step - 1
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def cesar(direction, text, shift):
#     if direction == 'encode':
#         encrypted_text=""
#         for letter in text:
#             index=alphabet.index(letter)
#             after_shift=index+shift
#             encrypted_text += alphabet[after_shift]
#         print(f"The encoded text is {encrypted_text}")
#     elif direction == "decode":
#         decrypted_text=""
#         for letter in text:
#             index=alphabet.index(letter)
#             after_shift=index-shift
#             decrypted_text += alphabet[after_shift]
#         print(f"The decoded text is {decrypted_text}")
#     else:
#         print("please choose correct direction..!")

# cesar(direction, text, shift)



from art import logo
          
def cesar(cipher_direction,start_text, shift_amount):
    Result=""
    if cipher_direction == "decode":
            shift_amount =shift_amount * -1
    for char in start_text:
        if char in alphabet:
            index=alphabet.index(char)
            new_index = index + shift_amount
            Result += alphabet[new_index]
        else:
            Result += char
    print(f"{cipher_direction}d result: ", Result)    
should_continue= True
while should_continue:
    print(logo)   
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift =shift%26
    cesar(direction, text, shift)
    ans=input("Type 'yes' if you want to go again. Otherwise type 'No'.").lower()
    if ans == "no":
        should_continue = False
        print("GoodBye...!")