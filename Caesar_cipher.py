import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
def caeser(plain_text,shift_amount,direction): 
    cipher_text = ""
    if direction=='decode':
        shift_amount*=-1
    for char in plain_text:
        if char in alphabet:    
            position=alphabet.index(char)
            new_position=position+shift_amount
            cipher_text+=alphabet[new_position]
        else:
            cipher_text+=char
    print(f"The {direction}d text is {cipher_text}")
    
should_continue=True
while should_continue==True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction=='encode' or direction=='decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift_amount = shift % 26
        caeser(text,shift,direction) 
        asking=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if asking=='no':
            should_continue=False
            print("Goodbye")
    else:
        print("ERROR!!! Please try again and type correctly")
        should_continue=False
    
