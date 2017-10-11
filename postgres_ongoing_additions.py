import psycopg2
import psycopg2.extras
import os
import shutil

def load_table():
	try:
		conn = psycopg2.connect(dbname='fantasy',host='localhost',user='postgres')
		print 'Connected'
	except:
		print 'Cant connect'

	cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

	path = 'C:\Users\Gary\Documents\\nfl\\all_data_max'

	# Currently stats test - change to stats after
	for file in os.listdir(path):
		if file.startswith('20'):
			data_import_sql = 'copy ' + 'fantasy.stats FROM \'C:\Users\Gary\Documents\\nfl\\all_data_max\\' + str(file) + '\' DELIMITER \',\' CSV HEADER;'
			#Activate the commented lines below once you figure out how to add the blank fields in the csvs. Add PPR fields as well.
			update_rec_pts = 'update fantasy.stats set rec_pts = (coalesce(receiving_yds,0)/10 +(coalesce(receiving_tds,0)*6));'
			update_rush_pts = 'update fantasy.stats set rush_pts = (coalesce(rushing_yds,0)/10 +(coalesce(rushing_tds,0)*6));'
			update_pass_pts = 'update fantasy.stats set pass_pts = (coalesce(passing_yds,0)/25 +(coalesce(passing_tds,0)*6));'
			update_tot_stnd_pts = 'update fantasy.stats set tot_pts = (coalesce(rec_pts,0)+coalesce(rush_pts,0)+coalesce(pass_pts,0)-(coalesce(fumbles_lost,0)*2));'
			update_rec_pts_ppr = 'update fantasy.stats set rec_pts_ppr = (coalesce(receiving_yds,0)/10 +(coalesce(receiving_tds,0)*6) + (coalesce(receiving_rec,0)));'
			update_rush_pts_ppr = 'update fantasy.stats set rush_pts_ppr = (coalesce(rushing_yds,0)/10 +(coalesce(rushing_tds,0)*6));'
			update_pass_pts_ppr = 'update fantasy.stats set pass_pts_ppr = (coalesce(passing_yds,0)/25 +(coalesce(passing_tds,0)*6));'
			update_tot_pts_ppr = 'update fantasy.stats set tot_pts_ppr = (coalesce(rec_pts_ppr,0)+coalesce(rush_pts_ppr,0)+coalesce(pass_pts_ppr,0)-(coalesce(fumbles_lost,0)*2));'
			cur.execute(data_import_sql)
			cur.execute(update_pass_pts)
			cur.execute(update_rush_pts)
			cur.execute(update_rec_pts)
			cur.execute(update_rec_pts_ppr)
			cur.execute(update_rush_pts_ppr)
			cur.execute(update_pass_pts_ppr)
			cur.execute(update_tot_stnd_pts)
			cur.execute(update_tot_pts_ppr)
			shutil.move('C:\Users\Gary\Documents\\nfl\\all_data_max\\'+file,
			'C:\Users\Gary\Documents\\nfl\\all_data_max\\clean_files\\'+file)
			conn.commit()


