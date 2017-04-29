
# create_shortcut.py - The original copy should be in home directory (/home/userca/)
#                    - Copy this file to desired directory and run to create a
#                    - a python shortcut to the desired directory
#                    - run the shortcut with "python shortcut_name.py"
#                    - you will be prompted for filename

# Input - filename (you will be prompted)
# Output - new .py file created in home directory

#!/usr/bin/env python

import os


# GET CURRENT DIRECTORY  (dir_path)
dir_path = os.path.dirname(os.path.realpath(__file__))
# os.chdir('/home/userca')
# print dir_path + "Pooap"

# GET FILE NAME
f_name = raw_input("Enter filename:")

# CREATE FILE WITH NAME FROM INPUT
# home_dir = "C:\\Test"  # for Wondows
home_dir = '/home/userca/'
baconFile = open(home_dir + f_name + '.py', 'w')

# FILL FILE CONTENTS
baconFile.write('import os\n')

baconFile.write('os.chdir("' + dir_path + '")\n')

exit_with_new_dir = 'os.system("/bin/bash")'
baconFile.write(exit_with_new_dir)

# os.chdir(dir_path)

#os.chdir("Documents/Java - How to Make a 2d Game/workspace/16-20")
# os.system("/bin/bash")
