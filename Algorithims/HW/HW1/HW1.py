# function to decode encrypted message
# takes in the encrypted message as a list and number shifted as an integer
# outputs nothing. prints the decrypted message as a string
def decoder(encrypted_message, shift_number):
    
    # decodes each letter by shifting back then prints the decrypted message
    decoded_message = ''

    for letter in encrypted_message:
        if(letter.isalpha() or letter.isdigit()):
            decoded_letter = chr(ord(letter) - shift_number)
        else:
            decoded_letter = letter
        
        decoded_message += decoded_letter


    print(f'Decrypted Message: {decoded_message}')



if __name__ == "__main__":

    # get user input (number 1-25)
    while(1):
        number = int(input("Enter a number between 1 and 25: "))

        if(number < 1 or number > 25):
            print(f'{number} is not between 1 and 25')
        else:
            break;

    # get string from user
    message = input("Enter a message to encrypt: ")

    # shift each letter ascii value in "message" by the "number" and put in "encrypted_array"
    encrypted_array = []

    for letter in message:
        if(letter.isalpha() or letter.isdigit()):
            shifted_letter = chr(ord(letter) + number)
        else:
            shifted_letter = letter
            
        encrypted_array.append(shifted_letter)

    # convert "encrypted_array" to a string "encrypted_message"
    encrypted_message = ''

    for letter in encrypted_array:
        encrypted_message += letter

    print(f'Encrypted Message: {encrypted_message}')

    # decode message
    decoder(encrypted_message, number)