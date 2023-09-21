# Simple Caesar Cipher Decoder program

# Declare a string variable that you would like to decode

string_to_decode = str(input("Enter a string that you would like to decode: ")) # str() to convert to a string

# Enter the number that represents the shift of the encoded string

shift_amount = int(input("Enter the numerical shift value of the encoded string: ")) # int() to convert to a int

shift_amount = shift_amount % 26 # Mod operator limits the shift amount to be inside the 26 lowercase alphabetical positions

# We will store the result in this list 

result = []

# Iterate through each letter in the string

for char in string_to_decode:

    # Check if the character is a space

    if char == " ":

        result.append(" ")
        continue
        
    # Conditional so that only alphabetical characters will be encoded

    if char.isalpha():  

        # Convert the character to its ASCII value

        char_ascii = ord(char)

        # Subtract the shift amount from the ASCII value

        char_ascii -= shift_amount

        # If the ASCII value is less than 65, then add 26 to the ASCII value
        # This is to ensure that the ASCII value is in this range as this range represents the valid chars of the alphabet 

        if char_ascii < 65:
                char_ascii += 26

        # Convert the ASCII value back to a character

        char = chr(char_ascii)

        # Add the char to the result list 

        result.append(char)

result = ''.join(result)

# Print the result

print("The decoded result is: " + result)