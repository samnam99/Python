import os

def get_filepaths(directory):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.

            # To get the directory and file name
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

            #To get the filename only
            #file_paths.append(filename)
    
    file_paths='\n'.join(file_paths) # Newline for each item.           
    return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.   
full_file_paths = get_filepaths("/Users/satishseshadri/001_Satish/Learn/")
print (full_file_paths)
