def process_file(input_filename, output_filename):
    """
    Read content from input file, process it, and write to output file.
    
    Args:
        input_filename (str): Name of the input file to read
        output_filename (str): Name of the output file to write
    
    Returns:
        bool: True if successful, False if an error occurred
    """
    try:
        # Step 1: Open and read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.readlines()
        
        # Step 2: Process the content
        modified_content = []
        for line in content:
            # Example modifications:
            # 1. Convert to uppercase
            # 2. Add line numbers
            # 3. Remove trailing whitespace
            modified_line = line.strip().upper()
            modified_content.append(modified_line)
        
        # Step 3: Write to output file
        with open(output_filename, 'w') as output_file:
            for i, line in enumerate(modified_content, 1):
                output_file.write(f"{i}. {line}\n")
        
        return True
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
        return False
    except PermissionError:
        print(f"Error: Permission denied when accessing the files.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return False

def main():
    """
    Main function to demonstrate file processing.
    Creates a sample input file and processes it.
    """
    # Create a sample input file
    sample_content = [
        "This is the first line\n",
        "Here's the second line\n",
        "And this is the third line"
    ]
    
    try:
        # Create sample input file
        with open('input.txt', 'w') as f:
            f.writelines(sample_content)
        
        # Process the file
        success = process_file('input.txt', 'output.txt')
        
        if success:
            print("File processing completed successfully!")
            
            # Display the results
            print("\nOriginal content:")
            with open('input.txt', 'r') as f:
                print(f.read())
            
            print("\nModified content:")
            with open('output.txt', 'r') as f:
                print(f.read())
    
    except Exception as e:
        print(f"An error occurred in the main function: {str(e)}")

if __name__ == "__main__":
    main()