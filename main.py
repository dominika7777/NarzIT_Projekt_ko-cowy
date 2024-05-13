import argparse


def parsearguments():
    parser = argparse.ArgumentParser(description='File Converter')
    parser.addargument('inputfile', help='Input file path')
    parser.addargument('output_file', help='Output file path')
    return parser.parse_args()

if __name == '__main':
    args = parse_arguments()
    print(f'Input file: {args.input_file}')
    print(f'Output file: {args.output_file}')