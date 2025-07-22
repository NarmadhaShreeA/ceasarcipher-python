
alpha =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Continues=False
while not Continues:
    direction=input("Type encode to encrypt, decode to decrypt: ")
    text=input("Enter the text:\n").lower()
    shift=int(input("Enter the shift:\n"))

    def encryption(original_text,No_of_shifts):
        encrypted_text=''
        for i in original_text:
            position = alpha.index(i)
            final_position=position + No_of_shifts
            encrypted_text+=alpha[final_position]
        return encrypted_text

    def decryption(decrypt_text,No_of_shifts):
        decrypted_text=''
        for i in decrypt_text:
            position=alpha.index(i)
            final_position=position - No_of_shifts
            decrypted_text+=alpha[final_position]
        return decrypted_text

    if direction=="encode":
        encrypted_text=encryption(text,shift)
        print(f"The encrypted text is , {encrypted_text}")

    elif direction=="decode":
        encrypted_text = encryption(text, shift)
        decrypted_text=decryption(text,shift)
        print(f"The decrypted text is, {decrypted_text}")

    stop_or_not=input("want to stop:\n").lower()
    if stop_or_not=="stop":
        Continues=True

    
        