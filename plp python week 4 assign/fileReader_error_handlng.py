# Simple file reader program with basic error handling
def read_file():
    # Keep asking for filename until successful or user quits
    while True:
        # Get filename from user
        print("\n=== Simple File Reader ===")
        filename = input("Enter the name of the file to read (or 'quit' to exit): ")
        
        # Check if user wants to quit
        if filename.lower() == 'quit':
            print("Thank you for using the file reader. Goodbye!")
            break
        
        try:
            # Try to open and read the file
            with open(filename, 'r') as file:
                # Read the contents
                contents = file.read()
                
                # Display the contents
                print("\n=== File Contents ===")
                print(contents)
                print("=== End of File ===")
                
                # Count lines, words, and characters
                lines = len(contents.splitlines())
                words = len(contents.split())
                chars = len(contents)
                
                # Display simple statistics
                print(f"\nFile Statistics:")
                print(f"Number of lines: {lines}")
                print(f"Number of words: {words}")
                print(f"Number of characters: {chars}")
                
        except FileNotFoundError:
            # Handle case when file doesn't exist
            print(f"Sorry, the file '{filename}' was not found.")
            print("Make sure you typed the filename correctly and it's in the same folder.")
            
        except PermissionError:
            # Handle case when file can't be accessed
            print(f"Sorry, can't access the file '{filename}'.")
            print("Make sure you have permission to read this file.")
            
        except Exception as e:
            # Handle any other unexpected errors
            print(f"An error occurred: {str(e)}")
        
        # Ask if user wants to try another file
        choice = input("\nWould you like to read another file? (yes/no): ")
        if choice.lower() != 'yes':
            print("Thank you for using the file reader. Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    read_file()