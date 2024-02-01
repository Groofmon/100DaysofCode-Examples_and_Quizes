# When we shift even 1 step after 'z' in alphabet while encrypting, program raises out of range error, as we may expect.
# But we solve this problem with defining an index number and if it is over lenght of alphabet, subtract it with lenght
#   of alphabet list. For example, when we try shift 1 digit on 'z', code detects index is out of range and subtract
#   with 26 and index gets equivalent to 0 and pick 'a' to prompt. So, We can shift how many times we want via this code

# But, Remember that this is not the exact or easiest way. There are a lot of another way to go,
# such as shift = shift % 25 code line. When it is over 25, code gets the mod of the shift. It works the same way
#   what we've done. We can implement this to the indexing to displaying to the monitor(encrypt_index).
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode():
    msg = input("Type your message to be encrypted:\n").lower().strip()
    encrypted_msg = [i for i in msg]
    shift_num = int(input("Type the shift number:\n"))
    for i in range(0, len(msg)):
        if encrypted_msg[i] == " ":
            continue

        encrypt_index = alphabet.index(msg[i]) + shift_num
        while encrypt_index >= 26:
            encrypt_index -= 26

        encrypted_msg[i] = alphabet[encrypt_index]
    print(f'Encoded message is \n{"".join(encrypted_msg)}')


def decode():
    msg = input("Type your encrypted message to be decrypted :\n").lower().strip()
    encrypted_msg = [i for i in msg]
    shift_num = int(input("Type the shift number:\n"))
    for i in range(0, len(msg)):
        if encrypted_msg[i] == " ":
            continue

        encrypt_index = alphabet.index(msg[i]) - shift_num
        while encrypt_index < 0:
            encrypt_index += 26

        encrypted_msg[i] = alphabet[encrypt_index]
    print(f'Decoded message is \n{"".join(encrypted_msg)}')


# MAIN PART
go_again = True
print("".join(['=' for i in "!!! WELCOME TO THE CEASAR CIPHER !!!"]))
print("!!! WELCOME TO THE CEASAR CIPHER !!!")
print("".join(['=' for ii in "!!! WELCOME TO THE CEASAR CIPHER !!!"]))

while go_again:
    operation = input("Type 'encode' or 'decode'\n").lower().strip()
    if operation == "decode":
        decode()
    elif operation == "encode":
        encode()
    again = input("Go again?\nType 'yes' if you want to go again. Otherwise type 'no'.\n    :").lower().strip()
    if again == "no":
        print("HAVE A GOOD DAY!")
        break

