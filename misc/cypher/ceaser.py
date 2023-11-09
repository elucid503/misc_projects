# Ask a user if they want to encode or decode 

mode = input("Enter 1 to use the Encoder or 2 for the Decoder: ")

# Check input 

while mode != "1" and mode != "2":
    print("Invalid input...")
    mode = input("Enter 1 to use the Encoder or 2 for the Decoder: ")

# If the user wants to encode

DisplayMode = "Encode"

if (mode == "2"):
    DisplayMode = "Decode"

# Declare a string variable that you would like to encode or decode 

entered_str = str(input(f"Enter a string that you would like to {DisplayMode}: ")) # str() to convert to a string

# Enter a number to shift the letters by

shift_amount = int(input("Enter a number to 'shift' letters by: ")) # int() to convert to a int

if (mode == "1"):

    # Because we have to 'step' through the string, we will store the result in this list 

    result = []

    # Iterate through each letter in the string

    for char in entered_str:
            
            # Conditional so that only alphabetical characters will be encoded

            if char.isalpha():  

                # Store if the character is upper case

                is_upper = char.isupper()
                
                # Convert all characters to lower case
                
                char = char.lower()

                # Find the characters position
                
                char_pos = ord(char) - ord('a')
                
                # Shift the characters by the desired amount
                # Mod operator limits the new position to be inside the 26 lowercase alphabetical positions

                char_pos = (char_pos + shift_amount) % 26 

                # Convert the characters new 'position' to it's alphabetical representation
                
                char = chr(char_pos + ord('a'))
                
                # Convert the character back to uppercase if appropiate

                if is_upper:
                    char = char.upper() 
            
            result.append(char) # add the character back to the result list 

    # Store the result (back in result) in a string created by joining the result list

    result = ''.join(result)

    # Print the result

    print("The encoded result is: " + result)

else: 

    shift_amount = shift_amount % 26 # Mod operator limits the shift amount to be inside the 26 lowercase alphabetical positions

    # We will store the result in this list 

    result = []

    # Iterate through each letter in the string

    for char in entered_str:

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