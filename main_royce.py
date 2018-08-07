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
	# Kinetic_Test_2
	SPREADSHEET_ID = '1e35U28DUeZJo5v2E16ICaq03AhojMjoBG1ZL9zRBN7Q'
	RANGE_ID = 'A2:P' 
	result = service.spreadsheets().values().get(
	    spreadsheetId=SPREADSHEET_ID, range=RANGE_ID).execute()
	values = result.get('values', [])

	#Create Folder Structures
	cwd = os.getcwd()
	# print(cwd)
	# print(os.listdir())
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
	sort_manufacturer(values)

def copy_media(old_title,new_title, asset_list, color = None):
	#what arguments do I need?
	# color(optional argument), product_title, path of master asset folder, name of new folder(color prepend)
	# pseudo code.
	cwd = os.getcwd()
	os.chdir('/Users/royceduong/Desktop/Clients/Kinetic_Society/kinetic_script/asset_library')
	if old_title in asset_list:
		os.chdir(old_title)
		if color in os.listdir():
			for root, dirs, files in os.walk(color):
				for item in files:
					path_file = os.path.join(root,item)
					shutil.copy2(path_file,cwd)
		else:
			print(os.listdir())
			for root, dirs, files in os.walk(os.getcwd()):
				for item in files:
					path_file = os.path.join(root,item)
					shutil.copy2(path_file,cwd)
	os.chdir(cwd)
	# chdir into asset_folder
	# find folder using old title
	# 	if folder has colors inside:
	# 		compare the color
	# 			chdir into color
	# 				copy everything inside of it. (shutil)
	# 	else:
	# 		copy everything inside (shutil)
	# print(os.getcwd())
	# print('copying' + old_title)
	# os.chdir(asset_folder_path)
	# folders = ls.dir
	# if old_title in folders:
	# 	print("we found the folder)")
	# else
	# 	print("folder not found")
	

def create_subfolders(variant,title,order_info):
	splt = variant.split('/ ')
	# TESTING TO GET ALL FOLDERS IN An ARRAY
	cwd = os.getcwd()
	os.chdir('/Users/royceduong/Desktop/Clients/Kinetic_Society/kinetic_script/asset_library')
	asset_list = os.listdir()
	os.chdir(cwd)

	if len(splt) > 1:
		clean_color = splt[1].strip()
		new_title = clean_color + ' - ' + title
		order_file = new_title + '.csv'
		if os.path.exists(new_title) or os.path.exists(order_file):
			add_to_file(new_title, order_file, order_info)
		if not os.path.exists(new_title) and not os.path.exists(order_file):
			create_new_folder_and_file(new_title, order_file, order_info)
			# print(os.getcwd())
			copy_media(title, new_title, asset_list, clean_color)	
			print('created: ' + new_title)
	else:
		order_file = title + '.csv'		
		if os.path.exists(title) or os.path.exists(order_file):
			add_to_file(title, order_file, order_info)
		if not os.path.exists(title) and not os.path.exists(order_file):
			create_new_folder_and_file(title, order_file, order_info)
			copy_media(title, title, asset_list)	

def sort_manufacturer(values):
	errors = []
	count = 0
	root_dir = os.getcwd()
	for v in values:
		count += 1
		orderfile = str(v[2]+'.csv')	
		# orderinfo = ['Order Number', 'Name', 'Number', 'Size']			
		orderinfo = [v[4],v[5],v[6],v[8]]
		title = v[2]	
		variant = v[9]
		if 'Hockey' in title or 'Baseball' in title or 'Soccer' in title:
			os.chdir('China')
			if 'Fully Stitched' in variant:
				os.chdir('fully_stitched')
				if variant:
					create_subfolders(variant,title,orderinfo)
				# else:
				# Add to error report
			elif 'Sublimation Print' in variant:
				os.chdir('sublimated')
				if variant:
					create_subfolders(variant,title,orderinfo)
			# else:
			# Add to error report
		elif 'Basketball' in title:
			if 'Sublimation Print' in variant:
				os.chdir('China')
				os.chdir('sublimated')
				if variant:
					create_subfolders(variant,title,orderinfo)
			elif 'Fully Stitched' in variant:
				os.chdir('Pakistan')
				os.chdir('fully_stitched')
				if variant:
					create_subfolders(variant,title,orderinfo)
			else:
				errors.append('Error on Order Number ' + v[15] + ': Print type is not listed')
		else:
			errors.append('Error on Order Number ' + v[15] + ': Jersey type not detected in product title')
			print(errors)
		os.chdir(root_dir)

		
# def copy_media():
# 	#Need to update logic for new folder names
# 	#Get list of order folders
# 	SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
# 	store = file.Storage('credentials.json')
# 	creds = store.get()
# 	if not creds or creds.invalid:
# 	    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
# 	    creds = tools.run_flow(flow, store)
# 	service = build('sheets', 'v4', http=creds.authorize(Http()))
	
# 	#Kinetic_Test_3
# 	SPREADSHEET_ID = '1BtSn51XYCmZNm7HuQrDibNTiGcn4_sm5aEWU1YDlazo'
# 	RANGE_ID = 'A2:P' 
# 	result = service.spreadsheets().values().get(
# 	    spreadsheetId=SPREADSHEET_ID, range=RANGE_ID).execute()
# 	values = result.get('values', [])	
# 	print(values)
	
# 	cwd = os.getcwd()
# 	order_directory = os.getcwd()
# 	os.chdir('test_assets')
# 	for x in os.listdir():
# 		if x in products_list:
# 			pass
if __name__ == "__main__":
	create_folders()
	# copy_media()