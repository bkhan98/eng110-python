# try:
#     file = open("order.txt")
# except FileNotFoundError as errmsg:
#     print("There has been an error!")
#     print(errmsg)

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#
# "a" - Append - Opens a file for appending, creates the file if it does not exist
#
# "w" - Write - Opens a file for writing, creates the file if it does not exist
#
# "x" - Create - Creates the specified file, returns an error if the file exists



def open_and_print_file(file):
    try:
        with open(file, "r") as file:
            for line in file.readlines():
                print(line.rstrip('\n'))
    except FileNotFoundError:
        print("File cannot be found")
        raise
    finally:
        print("\nExecution complete")

def write_to_file(file, order_item):
    try:
        with open(file, 'a') as file:
            file.write(order_item + '\n')

    except FileNotFoundError:
        print("File not found")
        raise

write_to_file("order.txt", "I can now add text to .txt files using python")

open_and_print_file("order.txt")
