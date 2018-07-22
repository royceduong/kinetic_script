### COPY MEDIA FUNCTION

def copy_media():
	#Need to update logic for new folder names
	#Get list of order folders
	cwd = os.getcwd()
	order_directory = os.getcwd()
	print(cwd)
	print(order_directory)

	order_names = os.listdir()
	if os.path.exists('orders'):
		order_names.remove('.DS_Store')
	# Get list of product folders
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

## END COPY MEDIA FUNCTION










def separate_colors(variants):
    colors = []
    for v in variants:
        splt = v.split("/ ")
        colors.push(spl[1])
    return colors

create_new_folder_and_file(folder_name, file_name):
    os.makedirs(folder_name)
    os.chdir(folder_name)
    with open(file_name, 'w', newline='') as csvfile:
        owriter = csv.writer(csvfile)
        owriter.writerow(['Order Number', 'Name', 'Number', 'Size'])
        owriter.writerow(orderinfo)
        csvfile.close()	

add_to_file(folder_name, file_name)
    if os.path.exists(folder_name):
        os.chdir(folder_name) #Go inside directory.
        with open(file_name, 'a', newline='') as csvfile: # open the csvfile with the same name
            owriter = csv.writer(csvfile)
            owriter.writerow(orderinfo)
            csvfile.close()	
            
(order_file, new_title, cwd):
if 'Fully Stitched' in variant:
    # print('Fully Stitched Row')
    os.chdir('fully_stitched')
    if v[9]:
        # print(v[9])
        splt = v[9].split('/ ')
        if len(splt) > 1:
            clean_color = splt[1].strip()
            new_title = clean_color + ' - ' + title
            order_file = new_title + '.csv'
            if os.path.exists(order_file) or os.path.exists(new_title):
                if os.path.exists(order_file):
                    os.chdir(order_file) #Go inside directory.
                    with open(order_file, 'a', newline='') as csvfile: # open the csvfile with the same name
                        owriter = csv.writer(csvfile)
                        owriter.writerow(orderinfo)
                        csvfile.close()	
            if not os.path.exists(order_file) and not os.path.exists(new_title):
                os.makedirs(order_file)
                os.chdir(order_file)
                with open(order_file, 'w', newline='') as csvfile:
                    owriter = csv.writer(csvfile)
                    owriter.writerow(['Order Number', 'Name', 'Number', 'Size'])
                    owriter.writerow(orderinfo)
                    csvfile.close()	
else:
    order_file = title + '.csv'		
    if os.path.exists(order_file) or os.path.exists(new_title):
        if os.path.exists(order_file):
            os.chdir(order_file) #Go inside directory.
            with open(order_file, 'a', newline='') as csvfile: # open the csvfile with the same name
                owriter = csv.writer(csvfile)
                owriter.writerow(orderinfo)
                csvfile.close()	
    if not os.path.exists(order_file) and not os.path.exists(new_title):
        os.makedirs(order_file)
        os.chdir(order_file)
        with open(order_file, 'w', newline='') as csvfile:
            owriter = csv.writer(csvfile)
            owriter.writerow(['Order Number', 'Name', 'Number', 'Size'])
            owriter.writerow(orderinfo)
            csvfile.close()		