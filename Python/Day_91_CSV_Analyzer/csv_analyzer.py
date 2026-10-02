import csv

FILE_NAME = "qc_sample_data.csv"

def analyze_csv(filename):
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        rows = list(reader)

        if not rows:
            print("The CSV file is empty.")
            return

        headers = rows[0]
        data_rows = rows[1:]

        row_count = len(data_rows)
        column_count = len(headers)

        print("=== CSV ANALYSIS ===")
        print(f"File       : {filename}")
        print(f"Rows       : {row_count}")
        print(f"Columns    : {column_count}")
        print(f"Column Names: {', '.join(headers)}")


analyze_csv(FILE_NAME)