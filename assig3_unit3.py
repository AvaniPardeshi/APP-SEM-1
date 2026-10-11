import csv
import json

def read_csv(input_path):
    with open(input_path, "r", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

def write_json(output_path, data):
    with open(output_path, "w") as f:
        json.dump(data, f, indent=4)

def convert_csv_to_json(input_path, output_path):
    data = read_csv(input_path)
    write_json(output_path, data)
    return data

if __name__ == "__main__":

    input_path = "students.csv"
    output_path = "students.json"

    data = convert_csv_to_json(input_path, output_path)

    print("CSV converted to JSON successfully!")
    print("Number of records:", len(data))
    print("JSON file created:", output_path)