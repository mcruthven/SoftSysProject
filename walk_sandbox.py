import os

def walk_sandbox ():
    """ This function traverses every directory in Sandbox, looks at every
        file, and then writes relevant metadata to a text file.
    """
    
    # The file name should be changed manually at this point in time
    text_file = open("soft_sys_sandbox_10_29_2012.txt", "w")

    # os.walk() will recursively walk through all the directories in <root> (in 
    # this case, X:\\) and find all the files in those directories
    for root, dirs, files in os.walk("X:\\"):

        # Look at every file in the current directory
        for f in files:
            
            # For some reason the path name of one of the files shows up as a
            # string of question marks and causes an error
            if "??" in f:
                continue
            
            else:
                # Get the path_name
                path_name = os.path.join(root, f)

                # Grab all the metadata you could ever want.  They were casted
                # to strings because write() was complaining
                metadata = os.stat(path_name)
                created = str(os.path.getctime(path_name))
                modified = str(metadata.st_mtime)
                accessed = str(metadata.st_atime)
                size = str(metadata.st_size)

                # path_name, time_created, last_modified, last_accessed, size
                write_data = "".join([path_name, " => ", created, " => ",
                                      modified, " => ", accessed, " => ", size,
                                      "\n"])

                # write() the data to the text file and print out where we are in
                # the walk; if write() fails, exit the program with False
                try:
                    text_file.write(write_data)
                    print "committed", path_name, "\n"
                    
                except:
                    print "failed to commit", path_name, "\n"
                    return False
                
    return True
                    
                            
if __name__ == "__main__":
    success = walk_sandbox()
    print success
    
   
