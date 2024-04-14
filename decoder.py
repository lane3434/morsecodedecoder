# Define Morse code dictionary
morse_code_dict = {
    'A': '.-', 'a': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.',
    ' ': '/'
}

def text_to_morse(text):
    morse_code = ''
    for char in text:
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            morse_code += char  # Keep non-alphanumeric characters as they are
    return morse_code

# Get user input
user_input = input("Enter text to convert to Morse code: ")

# Convert to Morse code
morse_output = text_to_morse(user_input)

# Save Morse code to file
with open("log.txt", "w") as file:
    file.write("Input Text: " + user_input + "\n")
    file.write("Morse Code: " + morse_output + "\n")

print("Morse Code saved to log.txt")
