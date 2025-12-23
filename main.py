from etl.extract import extract_excel
from etl.transform import transform_data
from etl.load import load_to_mysql

EXCEL_FILE_PATH = "data/employees.xlsx"
TABLE_NAME = "employees"

def main():
    print("Starting ETL process...")

    # Extract
    df = extract_excel(EXCEL_FILE_PATH)
    print("Data extracted")

    # Transform
    df = transform_data(df)
    print("Data transformed")

    # Load
    load_to_mysql(df, TABLE_NAME)
    print("Data loaded into MySQL successfully")

if __name__ == "__main__":
    main()
