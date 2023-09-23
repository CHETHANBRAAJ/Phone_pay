import csv
import psycopg2

# Database connection details


# CSV file path
csv_file_path = r"C:\Users\CHETHU\Downloads\map_user.csv"



# Specify the target table name in your database
table_name = 'map_user'

# Establish database connection


conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="phone_pay",
    user="postgres",
    password="Chethu@1999",
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Read CSV file and insert data into the database
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # Read the header to get column names
    print("CSV Header:", header)
    # Create the SQL query with placeholders for column names
    columns = ', '.join(header)
    placeholders = ', '.join(['%s'] * len(header))
    insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

    # Loop through the rows in the CSV and execute the insert query
    for row in csv_reader:
        cursor.execute(insert_query, row)

# Commit the changes to the database
conn.commit()

# Close the cursor and the database connection
cursor.close()
conn.close()

