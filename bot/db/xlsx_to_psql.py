import psycopg2
import openpyxl

excel_file = 'data/ETL.xlsx'

def create_table():
	# Open the Excel workbook and load the active sheet into a variable
	workbook = openpyxl.load_workbook(excel_file)
	sheet = workbook.active

	data = []
	# Iterate over the rows and append the data to the list
	for row in sheet.iter_rows(min_row = 3, values_only = True):
		data.append(row)


	connection = psycopg2.connect(
		database = 'postgres',
		user = 'postgres',
		password = 'admin',
		host = 'db',
		port = '5432'
	)
	cursor = connection.cursor()

	schema_name = 'public'
	table_name = 'overdue'

	schema_creation_query = f'CREATE SCHEMA IF NOT EXISTS {schema_name}'
	column_names = [column.value for column in sheet[1]]

	table_creation_query = f"""
	CREATE TABLE IF NOT EXISTS {schema_name}.{table_name} (
	{", ".join([f'"{name}" TEXT' for name in column_names])}
	)
	"""

	cursor.execute(schema_creation_query)
	cursor.execute(table_creation_query)

	insert_data_query = f"""
	   INSERT INTO {schema_name}.{table_name} ({", ".join([f'"{name}"' for name in column_names])})
	   VALUES ({", ".join(['%s' for _ in column_names])})
	"""

	cursor.executemany(insert_data_query, data)

	connection.commit()

	cursor.close()
	connection.close()

	# Print a message
	print('Import successfully completed!')

create_table()