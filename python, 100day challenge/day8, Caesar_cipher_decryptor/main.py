import logo

print(logo.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift, direction):
    cipher_text = ""

    for i in text:
        if i in alphabet:
            position = alphabet.index(i)
    
            if direction == "encode":
                position += shift
                if position > len(alphabet) - 1:
                    position -= len(alphabet)
                    
            elif direction == "decode":
                position -= shift
                if position < 0:
                    position += len(alphabet)
        
            cipher_text += alphabet[position]

        else:
            cipher_text += i
    
    print(f"The {direction} text is {cipher_text}")


end = False

while not end:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 25
    
    encrypt(text, shift, direction)

    replay = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    
    if replay == "no":
        end = True
        print("Good bey")