import csv
import json
import argparse

def parse_text_file(file_path):
    products = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        for i in range(0, len(lines), 4):
            try:
                product_id = lines[i].split(":")[1].strip()
                name = lines[i+1].split(":")[1].strip()
                price = lines[i+2].split(":")[1].strip()
                in_stock = lines[i+3].split(":")[1].strip()

                product = {
                    'ProductID': product_id,
                    'Name': name,
                    'Price': price,
                    'In_Stock': in_stock
                }

                products.append(product)
            except IndexError as e:
                print(f"Error parsing text file at line {i + 1}: {str(e)}")
    except FileNotFoundError:
        print(f"Text file not found: {file_path}")
    return products

def parse_csv_file(file_path):
    products = []
    try:
        with open(file_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                try:
                    product_id = row["Product ID"]
                    name = row['Name']
                    price = row['Price']
                    in_stock = row['In Stock']

                    product = {
                        'ProductID': product_id,
                        'Name': name,
                        'Price': price,
                        'InStock': in_stock
                    }

                    products.append(product)
                except (ValueError, KeyError) as e:
                    print(f"Error parsing CSV file at row {reader.line_num}: {str(e)}")
    except FileNotFoundError:
        print(f"CSV file not found: {file_path}")

    return products


parser = argparse.ArgumentParser(description='Parse product information from text and CSV files.')
parser.add_argument('text_file', help='Path to the text file (products.txt)')
parser.add_argument('csv_file', help='Path to the CSV file (products.csv)')
parser.add_argument('--output_file', help='Path to the JSON output file')

args = parser.parse_args()

text_products = parse_text_file(args.text_file)
csv_products = parse_csv_file(args.csv_file)

unified_data = text_products + csv_products

if args.output_file:
   with open(args.output_file, 'w') as json_file:
        json.dump(unified_data, json_file, indent=2)
   print(f"Data written to {args.output_file}")

print("Unified Product Data:")
print(unified_data)