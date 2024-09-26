def create_file():
    try:
        with open("my_file.txt", "w") as file:
            # Writing three lines to the file
            file.write("Hello, World!\n")
            file.write("This is line 2 with a number: 42\n")
            file.write("Final line here, with some text!\n")
        print("File created and written successfully.")
    except (PermissionError, OSError) as e:
        print(f"Error while writing to file: {e}")

def read_file():
    try:
        with open("my_file.txt", "r") as file:
            print("Contents of my_file.txt:")
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: The file 'my_file.txt' does not exist.")
    except (PermissionError, OSError) as e:
        print(f"Error while reading file: {e}")

def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            # Appending three lines to the file
            file.write("Appending line 1.\n")
            file.write("Appending line 2 with a number: 100.\n")
            file.write("Appending the final line!\n")
        print("Additional lines appended successfully.")
    except (PermissionError, OSError) as e:
        print(f"Error while appending to file: {e}")

def main():
    create_file()   # Create and write to the file
    read_file()     # Read and display the file's content
    append_to_file() # Append additional lines
    read_file()     # Read and display the file's content again

if __name__ == "__main__":
    main()
