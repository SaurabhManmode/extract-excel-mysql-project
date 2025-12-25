import pandas as pd
from faker import Faker

fake = Faker()

TOTAL_RECORDS = 1_000_000
BATCH_SIZE = 50_000   # safe chunk size
OUTPUT_FILE = "data/employees.xlsx"

def generate_batch(start_id, batch_size):
    data = []
    for i in range(batch_size):
        emp_id = start_id + i
        data.append({
            "id": emp_id,
            "name": fake.name(),
            "department": fake.random_element(
                elements=("IT", "HR", "Finance", "Sales", "Operations")
            ),
            "salary": fake.random_int(min=30000, max=150000)
        })
    return pd.DataFrame(data)

def generate_excel():
    writer = pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl")
    start_row = 0
    current_id = 1

    for _ in range(0, TOTAL_RECORDS, BATCH_SIZE):
        df = generate_batch(current_id, BATCH_SIZE)

        df.to_excel(
            writer,
            index=False,
            header=(start_row == 0),
            startrow=start_row
        )

        start_row += len(df)
        current_id += BATCH_SIZE

        print(f"Generated {start_row} records...")

    writer.close()
    print("✅ 1 million records Excel file created successfully")

if __name__ == "__main__":
    generate_excel()
