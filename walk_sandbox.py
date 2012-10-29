import os
import datetime

def walk_sandbox ():
    """ This function traverses every directory in Sandbox, looks at every
        file, and then writes relevant metadata to a text file.
    """
    
    # The file name should be changed manually at this point in time
    text_file = open("soft_sys_sandbox.txt", "a")
    
    # os.walk() will recursively walk through all the directories in <root> (in 
    # this case, X:\\) and find all the files in those directories
    for root, dirs, files in os.walk("X:\\"):

        # Look at every file in the current directory
        for f in files:
            
            # One of the files is written in a foreign language.  Lame.
            if "??" in f:
                continue
            
            else:
                # Get the path_name
                path_name = os.path.join(root, f)

                # Grab all the metadata you could ever want.  They were casted
                # to strings because write() was complaining
                metadata = os.stat(path_name)
                protection_bits = str(metadata.st_mode)
                inode_number = str(metadata.st_ino)
                num_hard_links = str(metadata.st_nlink)
                owner_user_id = str(metadata.st_uid)
                owner_group_id = str(metadata.st_gid)
                created = str(os.path.getctime(path_name)) # Only works on Windows
                modified = str(metadata.st_mtime)
                accessed = str(metadata.st_atime)
                size = str(metadata.st_size)

                write_data = "%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s\n" %(datetime.datetime.now(),
                                                                    path_name,
                                                                    protection_bits,
                                                                    inode_number,
                                                                    num_hard_links,
                                                                    owner_user_id,
                                                                    owner_group_id,
                                                                    created,
                                                                    modified,
                                                                    accessed,
                                                                    size)


                # write() the data to the text file and print out where we are in
                # the walk; if write() fails, print an error message and continue
                try:
                    text_file.write(write_data)
                    print "committed", path_name, "\n"
                    
                except:
                    print "FAILED TO COMMIT", path_name, "\n"
                    continue

    text_file.close()
    return True
                    
                            
if __name__ == "__main__":
    success = walk_sandbox()
    print success
    
   
