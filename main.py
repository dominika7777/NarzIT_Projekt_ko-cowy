import argparse
import json



class DataHandler:
    def __init__(self):
        self.data = {}

    def load_file(self, filename):
        file_extension = filename.split('.')[-1]
        if file_extension == 'json':
            self.load_json(filename)
        elif file_extension == 'yml':
            self.load_yaml(filename)
        elif file_extension == 'xml':
            self.load_xml(filename)
        else:
            print("Error: Unsupported file format.")

    def save_file(self, filename):
        file_extension = filename.split('.')[-1]
        if file_extension == 'json':
            self.save_json(filename)
        elif file_extension == 'yml' or file_extension == 'yaml':
            self.save_yaml(filename)
        elif file_extension == 'xml':
            self.save_xml(filename)
        else:
            print("Error: Unsupported file format.")

    def load_json(self, filename):
        with open(filename, 'r') as file:
            try:
                self.data = json.load(file)
                print("Loaded JSON data successfully.")
            except json.JSONDecodeError:
                print("Error: Invalid JSON syntax.")

    def save_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.data, file, indent=4)
        print("Data saved to JSON file successfully.")


def main():
    parser = argparse.ArgumentParser(description="Data File Handler")
    parser.add_argument("input_files", nargs=2, help="Input files and formats")
    args = parser.parse_args()

    input_files = args.input_files
    handler = DataHandler()

    filename, file_format = input_files[0].split('.')
    handler.load_file(filename + '.' + file_format)

    output_file = input_files[1]
    handler.save_file(output_file)



if __name__ == "__main__":
    main()