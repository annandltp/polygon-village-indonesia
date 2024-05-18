import pandas as pd

# Load the Excel file into a DataFrame
df = pd.read_excel(r"C:\Users\Anan\Desktop\Make Dashboard NJOP\Villages.xlsx")

# Define the SQL table name
table_name = "villages"

# Function to escape values (e.g., for SQL string formatting)
def escape_value(value):
    if isinstance(value, str):
        return "'{}'".format(value.replace("'", "''"))
    elif pd.isnull(value):
        return 'NULL'
    else:
        return str(value)

# Generate the SQL INSERT statements
insert_statements = []
for index, row in df.iterrows():
    columns = ', '.join(row.index)
    values = ', '.join(escape_value(value) for value in row)
    insert_statement = "INSERT INTO {} ({}) VALUES ({});".format(table_name, columns, values)
    insert_statements.append(insert_statement)

# Join all insert statements into a single string
insert_query = '\n'.join(insert_statements)

# Optionally, write the insert statements to a file
with open("insert_statements.sql", "w") as file:
    file.write(insert_query)

print("SQL INSERT statements generated successfully")
