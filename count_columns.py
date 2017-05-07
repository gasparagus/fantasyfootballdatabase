import csv
import os

# Counts number of rows for every file in clean_files folder

os.chdir('C:\Users\Gary\Documents\\nfl\\all_data_max\\clean_files\\')
directory = os.listdir('C:\Users\Gary\Documents\\nfl\\all_data_max\\clean_files\\')

for f in directory:
	with open(f) as file:
		r = csv.reader(file)
		for rows in r:
			if len(rows) == 36:
				print str(f), + len(rows)
			else:
				print str(f) + 'INCORRECT NUMBER OF ROWS'