# Simple Ceaser Cypher Encoder program 

# Declare a string variable that you would like to encode

string_to_encode = str(input("Enter a string that you would like to encode: ")) # str() to convert to a string

# Enter a number to shift the letters by

shift_amount = int(input("Enter a number to 'shift' letters by: ")) # int() to convert to a int

# Check if shift_amount is greater than 25, and return an error warning if it is

if shift_amount > 25:
     
        print("Error: Shift amount must be less than 25")
        
        exit() # exit the program

# Because we have to 'step' through the string, we will store the result in this list 

result = []

# Iterate through each letter in the string

for char in string_to_encode:
        
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