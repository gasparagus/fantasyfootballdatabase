import psycopg2
import psycopg2.extras
import os

try:
	conn = psycopg2.connect(dbname='fantasy',host='localhost',user='postgres')
	print 'Connected'
except:
	print 'Cant connect'

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


path = 'C:\Users\Gary\Documents\\nfl\\all_data_max\\clean_files'

strng = "(year int4, week int4, name varchar (30),	id int4,	home varchar (10),	team varchar (3),	pos varchar (5),	defense_ast float8,	defense_ffum float8,	defense_int float8,	defense_int_yds float8,	defense_qbhit float8,	defense_sk float8,	defense_tkl float8,	defense_tkl_loss float8,	first_down float8,	fumbles_forced float8,	passing_att float8,	passing_cmp float8,	passing_first_down float8,	passing_incmp float8,	passing_int float8,	passing_tds float8,	passing_yds float8,	receiving_lng float8,	receiving_rec float8,	receiving_tar float8,	receiving_tds float8,	receiving_yac_yds float8,	receiving_yds float8,	rushing_att float8,	rushing_first_down float8,	rushing_lng float8,	rushing_tds float8,	rushing_yds float8,	third_down_att float8,	third_down_conv float8,	third_down_failed float8);"
rep = strng.replace('	',' ')
rep_str = str(rep)

# Will need to replace create table with an insert statement
for file in os.listdir(path):
	str_file = str(file).replace('.csv','')
	print str_file
	table = 'CREATE TABLE IF NOT EXISTS fantasy' +'.nfl_' + str_file + rep_str
	cur.execute(table)
	conn.commit()
	data_import_sql = 'copy ' + 'fantasy.nfl_' + str_file + ' FROM \'C:\Users\Gary\Documents\\nfl\\all_data_max\\clean_files\\' + file + '\' DELIMITER \',\' CSV HEADER;'
	cur.execute(data_import_sql)
	conn.commit()
conn.close()


