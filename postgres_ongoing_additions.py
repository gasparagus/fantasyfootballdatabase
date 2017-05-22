import psycopg2
import psycopg2.extras
import os
import shutil

try:
	conn = psycopg2.connect(dbname='fantasy',host='localhost',user='postgres')
	print 'Connected'
except:
	print 'Cant connect'

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

path = 'C:\Users\Gary\Documents\\nfl\\all_data_max'

for file in os.listdir(path):
	if file.startswith('20'):
		data_import_sql = 'copy ' + 'fantasy.stats FROM \'C:\Users\Gary\Documents\\nfl\\all_data_max\\' + str(file) + '\' DELIMITER \',\' CSV HEADER;'
		cur.execute(data_import_sql)
		conn.commit()
	conn.close()
	shutil.move('C:\Users\Gary\Documents\\nfl\\all_data_max\\'+file,
	'C:\Users\Gary\Documents\\nfl\\all_data_max\\clean_files\\'+file)


