def read_file():
    filename=input("Enter the file name: ")
    try:
        with open(filename, 'r') as file:
            data = file.read()
            print("File content: ")
            print(data)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        
read_file()