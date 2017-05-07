import pandas as pd
import os
import shutil

# Removes all columns except the ones listed below and moves to clean_files folder.

columns_to_keep = ['name',
'id',
'home',
'team',
'pos',
'defense_ast',
'defense_ffum',
'defense_int',
'defense_int_yds',
'defense_qbhit',
'defense_sk',
'defense_tkl',
'defense_tkl_loss',
'first_down',
'fumbles_forced',
'passing_att',
'passing_cmp',
'passing_first_down',
'passing_incmp',
'passing_int',
'passing_tds',
'passing_yds',
'receiving_lng',
'receiving_rec',
'receiving_tar',
'receiving_tds',
'receiving_yac_yds',
'receiving_yds',
'rushing_att',
'rushing_first_down',
'rushing_lng',
'rushing_tds',
'rushing_yds',
'third_down_att',
'third_down_conv',
'third_down_failed']


def clean_columns():
	directory = os.listdir('C:\Users\Gary\Documents\\nfl\\all_data_max')
	for file in directory:
		if file.startswith('20'):
			# Reads csv with Pandas.
			f = pd.read_csv(file)
			# Creates a new Data Frame without the columns in the list above.
			new_file = f[columns_to_keep]
			# Strips out all the zeros from the ids on the left (not sure why all zeros, but works)
			# Only works after processing once.
			new_file['id'] = new_file['id'].str.replace('00-','0')
			new_file['id'] = new_file['id'].str.replace('XX-','0')
			file_name = str(file)
			year = file_name.split('_')
			week = year[1].split('.')
			new_file.insert(0,'week',str(week[0]))
			new_file.insert(0,'year',str(year[0]))
			# Creates new csv from Data Frame.
			new_file.to_csv(file_name, index=False)
			shutil.move('C:\Users\Gary\Documents\\nfl\\all_data_max\\'+file_name,
				'C:\Users\Gary\Documents\\nfl\\all_data_max\\clean_files\\'+file_name)
