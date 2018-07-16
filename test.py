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