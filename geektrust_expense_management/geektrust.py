from sys import argv
from src.business_logic.process_commands import Process
def main():

    ALLOWED_VALUES= 2
    if len(argv) != ALLOWED_VALUES:
        raise Exception("File path not entered")

    FILE_FLAG_INDEX = 1
    file_path = argv[FILE_FLAG_INDEX]
    f = open(file_path, 'r')
    lines = f.readlines()

    object_process = Process()
    # send all lines to get processed
    object_process.process_all_lines(lines)

if __name__ == "__main__":
    main()