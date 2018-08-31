import psycopg2
import psycopg2.extras
import os
import shutil

def load_table():
	try:
		conn = psycopg2.connect(dbname='fantasy',host='localhost',user='postgres')
		print 'Connected for file load'
	except:
		print 'Cant connect'

	cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

	path = 'C:\Users\Gary\Documents\\nfl\\all_data_max'
	#delete only rows for 2018 and reload full year to date
	cur.execute('delete from fantasy.stats where year = \'2018\'')
	print 'All rows from 2018 deleted'

	# Currently stats test - change to stats after
	for file in os.listdir(path):
		if file.startswith('20'):
			data_import_sql = 'copy ' + 'fantasy.stats FROM \'C:\Users\Gary\Documents\\nfl\\all_data_max\\' + str(file) + '\' DELIMITER \',\' CSV HEADER;'
			cur.execute(data_import_sql)
			print 'Successfully copied ' + str(file) + ' to table.'
			conn.commit()
			shutil.move('C:\Users\Gary\Documents\\nfl\\all_data_max\\'+file,'C:\Users\Gary\Documents\\nfl\\all_data_max\\clean_files\\'+file)
			print 'Successfully copied file to clean_files folder.'
			#Activate the commented lines below once you figure out how to add the blank fields in the csvs. Add PPR fields as well.
	
def update_points():
	try:
		conn = psycopg2.connect(dbname='fantasy',host='localhost',user='postgres')
		print 'Connected for point updates'
	except:
		print 'Cant connect'
	cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
	update_rec_pts = 'update fantasy.stats set rec_pts = (coalesce(receiving_yds,0)/10 +(coalesce(receiving_tds,0)*6));'
	update_rush_pts = 'update fantasy.stats set rush_pts = (coalesce(rushing_yds,0)/10 +(coalesce(rushing_tds,0)*6));'
	update_pass_pts = 'update fantasy.stats set pass_pts = (coalesce(passing_yds,0)/25 +(coalesce(passing_tds,0)*6));'
	update_tot_stnd_pts = 'update fantasy.stats set tot_pts = (coalesce(rec_pts,0)+coalesce(rush_pts,0)+coalesce(pass_pts,0)-(coalesce(fumbles_lost,0)*2));'
	update_rec_pts_ppr = 'update fantasy.stats set rec_pts_ppr = (coalesce(receiving_yds,0)/10 +(coalesce(receiving_tds,0)*6) + (coalesce(receiving_rec,0)));'
	update_rush_pts_ppr = 'update fantasy.stats set rush_pts_ppr = (coalesce(rushing_yds,0)/10 +(coalesce(rushing_tds,0)*6));'
	update_pass_pts_ppr = 'update fantasy.stats set pass_pts_ppr = (coalesce(passing_yds,0)/25 +(coalesce(passing_tds,0)*6));'
	update_tot_pts_ppr = 'update fantasy.stats set tot_pts_ppr = (coalesce(rec_pts_ppr,0)+coalesce(rush_pts_ppr,0)+coalesce(pass_pts_ppr,0)-(coalesce(fumbles_lost,0)*2));'
	cursor.execute(update_pass_pts)
	print 'Passing points updated!'
	cursor.execute(update_rush_pts)
	print 'Rushing points updated!'
	cursor.execute(update_rec_pts)
	print 'Reception points updated!'
	cursor.execute(update_rec_pts_ppr)
	print 'Reception points updated (PPR)!'
	cursor.execute(update_rush_pts_ppr)
	print 'Rushing points updated! (PPR)'
	cursor.execute(update_pass_pts_ppr)
	print 'Passing points updated! (PPR)'
	cursor.execute(update_tot_stnd_pts)
	print 'Total points updated!'
	cursor.execute(update_tot_pts_ppr)
	print 'Total points updated! (PPR)'
	conn.commit()