from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import shutil
import os
import csv


def create_new_folder_and_file(folder_name, file_name, orderinfo):
    os.makedirs(folder_name)
    os.chdir(folder_name)
    with open(file_name, 'w', newline='') as csvfile:
        owriter = csv.writer(csvfile)
        owriter.writerow(['Order Number', 'Name', 'Number', 'Size'])
        owriter.writerow(orderinfo)
        csvfile.close()	

def add_to_file(folder_name, file_name, orderinfo):
	if os.path.exists(folder_name):
		os.chdir(folder_name)
		with open(file_name, 'a', newline='') as csvfile: # open the csvfile with the same name
			owriter = csv.writer(csvfile)
			owriter.writerow(orderinfo)
			csvfile.close()	

def create_folders():
	# Setup the Sheets API
	SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
	store = file.Storage('credentials.json')
	creds = store.get()
	if not creds or creds.invalid:
	    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
	    creds = tools.run_flow(flow, store)
	service = build('sheets', 'v4', http=creds.authorize(Http()))
	
	# Call the Sheets API
	# SPREADSHEET_ID = '1xNN28kbO9WpPSCW-FABLr8mT6f11kjVsbszAizil0d8'
	SPREADSHEET_ID = '1e35U28DUeZJo5v2E16ICaq03AhojMjoBG1ZL9zRBN7Q'
	
	#Running from row 681 and below
	RANGE_ID = 'A2:P' 
	result = service.spreadsheets().values().get(
	    spreadsheetId=SPREADSHEET_ID, range=RANGE_ID).execute()
	values = result.get('values', [])

	#Create Folder Structures
	cwd = os.getcwd()
	if not os.path.exists('Orders'):
	    os.makedirs('Orders')
	os.chdir('Orders')
	ordersDir = os.getcwd()
	if not os.path.exists('China'):
		os.makedirs('China')
		os.chdir('China')
		if not os.path.exists('fully_stitched'):
			os.makedirs('fully_stitched')
		if not os.path.exists('sublimated'):
			os.makedirs('sublimated')
	os.chdir(ordersDir)
	if not os.path.exists('Pakistan'):
		os.makedirs('Pakistan')
		os.chdir('Pakistan')
		if not os.path.exists('fully_stitched'):
			os.makedirs('fully_stitched')
		if not os.path.exists('sublimated'):
			os.makedirs('sublimated')
	
	# Reset to root directory
	os.chdir(ordersDir)
	#Create subfolders
	# create_subfolders(values,colors)
	sort_manufacturer(values)
	
def sort_manufacturer(values):
	errors = []
	count = 0
	root_dir = os.getcwd()
	for v in values:
		count += 1
		print(count)
		orderfile = str(v[2]+'.csv')				
		orderinfo = [v[4],v[5],v[6],v[8]]				# orderinfo = ['Order Number', 'Name', 'Number', 'Size']
		variant = str(v[9]).replace('/','-')
		title = v[2]	
		if 'Hockey' in title or 'Baseball' in title or 'Soccer' in title:
			os.chdir('China')
			if 'Fully Stitched' in variant:
				os.chdir('fully_stitched')
				if v[9]:
					splt = v[9].split('/ ')
					if len(splt) > 1:
						clean_color = splt[1].strip()
						new_title = clean_color + ' - ' + title
						order_file = new_title + '.csv'
						if os.path.exists(new_title) or os.path.exists(order_file):
							add_to_file(new_title, order_file, orderinfo)
						if not os.path.exists(new_title) and not os.path.exists(order_file):
							create_new_folder_and_file(new_title, order_file, orderinfo)	
					else:
						order_file = title + '.csv'		
						if os.path.exists(title) or os.path.exists(order_file):
							add_to_file(title, order_file, orderinfo)
						if not os.path.exists(title) and not os.path.exists(order_file):
							create_new_folder_and_file(title, order_file, orderinfo)
				# else:
				# 	errors.append('Error on Order Number ' + v[15] + ': Variant not detected')					
			elif 'Sublimation Print' in variant:
				os.chdir('sublimated')
				if v[9]:
					splt = v[9].split('/ ')
					if len(splt) > 1:
						cleaned_color_str = splt[1].strip()
						new_title = cleaned_color_str + ' - ' + title
						order_file = new_title + '.csv'
						if os.path.exists(order_file) or os.path.exists(new_title):
							add_to_file(new_title, order_file, orderinfo)
						if not os.path.exists(order_file) and not os.path.exists(new_title):
							create_new_folder_and_file(new_title, order_file, orderinfo)
					else:
						order_file = title + '.csv'		
						if os.path.exists(title) or os.path.exists(order_file):
							add_to_file(title, order_file, orderinfo)
						if not os.path.exists(title) and not os.path.exists(order_file):
							create_new_folder_and_file(title, order_file, orderinfo)
			# else:
			# 	errors.append('Error on Order Number ' + v[15] + ': Print type is not listed')
		elif 'Basketball' in title:
			if 'Sublimation Print' in variant:
				os.chdir('China')
				os.chdir('sublimated')
				if v[9]:
					splt = v[9].split('/ ')
					if len(splt) > 1:
						cleaned_color_str = splt[1].strip()
						new_title = cleaned_color_str + ' - ' + title
						order_file = new_title + '.csv'
						if os.path.exists(order_file) or os.path.exists(new_title):
							add_to_file(new_title, order_file, orderinfo)
						if not os.path.exists(order_file) and not os.path.exists(new_title):
							create_new_folder_and_file(new_title, order_file, orderinfo)
					else:
						order_file = title + '.csv'		
						if os.path.exists(title) or os.path.exists(order_file):
							add_to_file(title, order_file, orderinfo)
						if not os.path.exists(title) and not os.path.exists(order_file):
							create_new_folder_and_file(title, order_file, orderinfo)
			elif 'Fully Stitched' in variant:
				os.chdir('Pakistan')
				os.chdir('fully_stitched')
				if v[9]:
					splt = v[9].split('/ ')
					if len(splt) > 1:
						cleaned_color_str = splt[1].strip()
						new_title = cleaned_color_str + ' - ' + title
						order_file = new_title + '.csv'
						if os.path.exists(order_file) or os.path.exists(new_title):
							add_to_file(new_title, order_file, orderinfo)
						if not os.path.exists(order_file) and not os.path.exists(new_title):
							create_new_folder_and_file(new_title, order_file, orderinfo)
					else:
						order_file = title + '.csv'		
						if os.path.exists(title) or os.path.exists(order_file):
							add_to_file(title, order_file, orderinfo)
						if not os.path.exists(title) and not os.path.exists(order_file):
							create_new_folder_and_file(title, order_file, orderinfo)
			else:
				errors.append('Error on Order Number ' + v[15] + ': Print type is not listed')
		else:
			errors.append('Error on Order Number ' + v[15] + ': Jersey type not detected in product title')
			print(errors)
		os.chdir(root_dir)

		
def copy_media():
	#Need to update logic for new folder names
	#Get list of order folders
	cwd = os.getcwd()
	order_directory = os.getcwd()
	
	order_names = os.listdir()
	if os.path.exists('orders'):
		order_names.remove('.DS_Store')
	#Get list of product folders
	os.chdir('..')
	os.chdir('Products')
	products_directory = os.getcwd()
	product_names = os.listdir()
	product_names.remove('.DS_Store')
	movable = []
	for path, dirs, files in os.walk('.'):
		for p in dirs or files:
			print(p)

	#product_names.remove('.DS_Store')
	os.chdir(cwd)
	directory_list = []
	moveable = []
	for path, dirs, files in os.walk('.'):
		print(dirs)
		if dirs in product_names:
			movable.append(dirs)
			print(dirs)
		if files in product_names:
			movable.append(files)
			print(files)
	#print(directory_list)
	#print(movable)
	#print(movable)
	
	for x in os.walk('.'):
		y = next(os.walk('.'))
		print(y)

	movable = list(set(order_names) & set(product_names))

	#Copy media files from Product folder if they have the same folder name
	movable = list(set(order_names) & set(product_names))
	if movable:
		for move_from in movable:
			copy_from = products_directory + '/' + move_from
			copy_items = []
			for c in os.listdir(copy_from):
				copy_items.append(c)
			#copy_items.remove('.DS_Store')

			copy_to = order_directory + '/' + move_from
			for copy_to in copy_items:
				copy_from_item = copy_from + '/' + copy_to
				#shutil.copy(copy_from_item, copy_to)
		print('Matching folders media has been copied over.')
	else:
		print('No items were copied over due to no matching folder names')
	
if __name__ == "__main__":
	create_folders()
	#copy_media()