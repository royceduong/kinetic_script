This project is for Kinetic Society, a custom athletic apparel company based in Los Angeles, CA.
This script will automate the creation of digital assets for their manufactueres in China and Pakistan.


Create a script/algorithm
    -Takes data from Excel Document and creates folders/file structures ready for manufacturers
	Functions
		-def create_new_folder_and_file(folder_name, file_name, orderinfo)
			creates the first folder and first file
			writes the first row of order information
		
		-def add_to_file(folder_name, file_name, orderinfo)
			adds rows to existing orders with same name

        -def create_folders():
            -get request from Google Spreadsheet
            -Creates China and Pakistan folders
                -Creates "fully_stitched" and "sublimation" folders in each
        
        -def sort_manufacturer(values):
			determines if each row belongs to china or Pakistan
			checks for "color variants"
				if there is a color variant, prepend the product title
				Variant format must be {Print Type} / {Color}
					i.e. Fully Stitched / Blue


		To Do List
			Not catching rows without colors in variant (DONE)
			Incorrect folder names, they are created with file names (DONE)
			Refactor - folder and file creation. (DONE)
			
			create error report
				make every "else" conditional append an error report

				Create csv file (save the path so it can be accessed globally)
				array is full of errors
				iterate through array to insert errors

				Potential errors
					Does not meet conditionals
						No Jersey Type in Product title
						No fully stitched or sublimation in variant
					If Subfolders are removed, def create_folders does not catch. Code will break.
						ie. Removed fully stitched from China. It will break.
					What are the best practices for something like this?
		

			Copy Media Function (DONE)
				Copy media will be implemented when the new order folder is created.
				copy_media(color, product_title):
					chdir(asset_folder)
					if we find a "Color" folder:
						for x in <Color Folder>:
							if color == x:
								chdir(color)
									for each file in folder:
										shutil.copy(current file, copy_file)
					else:
						Loop for product_title matches
							if product_title == product_title:
								chdir(product_title)
								for each file in folder:
									shutil.copy(current_file, copy_file)


Work Day Tues. August 7 7:30am.
Tasks
Write Copy_Media Function
	1. find the path to asset library
	2. rework the color conditional. 



create a test spreadsheet (DONE) => properly tests copy functionality against naming conventions
	Identify jerseys that have color subfolders.
		aKDPHI - Standard Issue Baseball Jersey
		Chi Phi - House Basketball Jersey
		Kappa Sigma - Standard Issue Baseball Jersey
		Kinetic ID - LA Skyline Baseball Jersey
		
	Identify jersesys that DO NOT have color subfolders.

	Buggy folders
		In Test Sheet
		KAPPA SIGMA - SOUTH BEACH Basketball JERSEY (will lowercase Basketball create issues?)
			YES. Yes, it does create issues. Extra credit to normalize all text.. but probably easier to just control the naming conventions
		
		Not in Test Sheet 
		ALPHA EPSILON PHI - SOUTH BEACH BASKETBALL JERSEY (has empty subfolder inside with another jersey name)
			It does not become an issue as folder traversal into color folder only happens upon positive matches.
		
