import os
import time
import stat
from os.path import join, getsize



for root, dirs, files in os.walk("X:\\"):
    print "root: ", root
    print "dirs: ", dirs
    print "files: ", files
    print "_-------------------------_"
    for f in files:
        path = os.path.join(root, f)
        
        print path
        st = os.stat(path)
        
        print "last accessed", "=>", time.ctime(st[stat.ST_ATIME])
    print "-----------------------------"
   
