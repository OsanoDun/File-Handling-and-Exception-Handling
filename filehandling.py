# File Read & Write Challenge + Error Handling Lab

# Ask the user for a filename
filename = input("Enter the filename to read: ")

try:
    # Read the contents of the provided filename
    with open(filename, "r") as file:
        content = file.read()

    # Count the number of words
    word_count = len(content.split())

    # Convert all text to uppercase
    content_upper = content.upper()

    # Create a new output filename based on the input
    output_filename = "output.txt"

    # Write the processed text and the word count to the new output file
    with open(output_filename, "w") as file:
        file.write(content_upper)
        file.write(f"\n\nWord Count: {word_count}")

    # Print a success message
    print(f"Success! '{output_filename}' has been created with the processed text and word count.")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except IOError:
    print(f"Error: Could not read the file '{filename}'.")