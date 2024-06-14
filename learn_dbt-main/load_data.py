import pandas as pd
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def generate_insert_sql(csv_file_path, table_name):
    df = pd.read_csv(csv_file_path)
    columns = df.columns
    
    logging.info(f"Columns in {csv_file_path}: {columns}")
    
    sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES\n"
    for index, row in df.iterrows():
        values = []
        for value in row:
            if pd.isna(value):
                values.append("NULL")
            elif isinstance(value, str):
                value = value.replace("'", "''")  # Escape single quotes in strings
                values.append(f"'{value}'")
            elif isinstance(value, int):
                values.append(str(value))  # Integers are added directly as strings
            elif isinstance(value, float):
                values.append(str(value))  # Floats are also added directly as strings
            elif isinstance(value, bytes):
                value = value.hex()
                values.append(f"E'\\\\x{value}'")
            else:
                values.append(str(value))
        sql += f"    ({', '.join(values)}),\n"
    sql = sql.rstrip(",\n") + ";"
    return sql

def generate_inserts_for_multiple_csv(csv_files):
    insert_statements = {}
    for csv_file_path, table_name in csv_files.items():
        insert_sql = generate_insert_sql(csv_file_path, table_name)
        insert_statements[table_name] = insert_sql
    return insert_statements

# Contoh penggunaan
csv_files = {
    "categories.csv": "categories",
    "customers.csv": "customers",
    "employee_territories.csv": "employee_territories",
    "employees.csv": "employees",
    "order_details.csv": "order_details",
    "orders.csv": "orders",
    "products.csv": "products",
    "regions.csv": "regions",
    "shippers.csv": "shippers",
    "suppliers.csv": "suppliers",
    "territories.csv": "territories"
}

print("Generating insert statements...")
insert_statements = generate_inserts_for_multiple_csv(csv_files)

with open("insertData.sql", "w") as file:
    for table_name, insert_sql in insert_statements.items():
        file.write(f"-- Insert statements for table: {table_name}\n")
        file.write(insert_sql)
        file.write("\n\n")
        
        
print("Insert statements generated successfully.")