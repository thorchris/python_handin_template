import argparse
import csv

def print_file_content(file):
    """print content of a csv file to the console"""
    file_object = open(file)
    content = file_object.read()
    print(content)


def write_list_to_file(output_file, lst):
    """take a list or tuple and write each element to a new line in file"""
    file_object = open(output_file, 'w')
    file_object.write('\n'.join(lst))


def read_file(input_file):
    """take a csv file and read each row into a list"""
    with open(input_file, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        print(data)


if __name__ == "__main__":
    """run with python w2.py input.txt -f output.txt -l word1 word2 word3"""
    parser = argparse.ArgumentParser(description='Solution to handin week 2')
    parser.add_argument('input_file', help='the input file to consume')
    parser.add_argument('-l', '--list', nargs='*', help='extra words', required=False) # nargs='*' means 0 or more args, nargs='+' means 1 or more
    parser.add_argument('-f', '--output_file', help='the file to print to. (console if nothing is given)')
    args = parser.parse_args()
    print('INPUT:', args.input_file)
    print('File:', args.output_file)
    print('Len', vars(args))

    # only first arg
    if not (args.output_file and args.list):
        print_file_content(args.input_file)
    # only input and output
    else:
        lst = read_file(args.input_file)
        if args.list:
            lst.extend(args.list)
        print('LISTEN:',lst)
        write_list_to_file(args.output_file,lst)