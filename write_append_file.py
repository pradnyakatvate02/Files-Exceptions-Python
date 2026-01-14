# Task 2: Write and append data to a file

data = input("Enter some data: ")

# Write data to file
with open("output.txt", "w") as file:
    file.write(data + "\n")

# Append additional data
with open("output.txt", "a") as file:
    file.write("This is appended data.\n")

# Read and display file content
with open("output.txt", "r") as file:
    print("\nFinal content of the file:")
    print(file.read())
