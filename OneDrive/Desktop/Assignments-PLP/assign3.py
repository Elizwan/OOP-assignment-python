def read_and_write_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify content (convert to uppercase in this example)
        modified_content = content.upper()

        # Open the output file in write mode
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"File '{input_filename}' was read and written successfully to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError as e:
        print(f"Error: An issue occurred while reading or writing the file. Details: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Test the function
input_file = input("Enter the input filename: ")
output_file = input("Enter the output filename: ")

read_and_write_file(input_file, output_file)


#2
def open_file_with_error_handling():
    filename = input("Enter the filename: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except IOError as e:
        print(f"Error: An issue occurred while trying to read the file. Details: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Test the error handling function
open_file_with_error_handling()
