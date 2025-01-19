import psycopg2
import openpyxl
from openpyxl import Workbook

def get_xlsx():

	connection = psycopg2.connect(
		database = 'postgres',
		user = 'postgres',
		password = 'admin',
		host = 'db',
		port = '5432'
	)
	cursor = connection.cursor()

	select_data_query = f"""
		select "Субъект РФ", sum ("Количество Доз"::float) as "Количество Доз", round(avg ("Просрочено дней"::float)) as "Просрочено дней"
		from public.overdue 
		group by "Субъект РФ"
		order by "Субъект РФ"
	"""
	head = (("Субъект РФ", "Суммарное количество доз", "Среднее просрочено дней"))
	cursor.execute(select_data_query)
	data = cursor.fetchall()
	connection.commit()

	cursor.close()
	connection.close()

	book = Workbook()
	sheet = book.active
	sheet.append(head)
	for row in data:
		sheet.append(row)
	book.save ('data/result.xlsx')

