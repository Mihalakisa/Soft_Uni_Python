from io import open


def print_contents(file_path):
    try:
        file = open(file_path)
        print(file.read())
        print("File found")
    except FileNotFoundError:
        print("File not found")


print_contents("./text.txt")
