#!/usr/bin/python
import commands
import os


# add your new line here "path + scriptname"
newscriptadd = "https://svn-repopa.th/svn/path/to/scriptname.py scriptname.py"

# we can also remove lines
remove_lines = ["https://svn-repopa.th/svn/path/to/scriptname.py scriptname.py","https://svn-repopa.th/svn/path/to/scriptname2.py scriptname2.py"]

# your svn client path
svn_client_path = "/my/local/path/to/svn/checkout/"


#######
#######  PLEASE SET THE ABOVE VARIABLES
#######


for foldername in os.listdir(svn_client_path):
    # tmp file for write and read
    writefile = "/tmp/propsettmp.txt"
    file = open(writefile , "w")

    # get all the current lines of the looped folder
    cmd = "svn proplist --verbose " + svn_client_path + foldername
    cmd_out = os.popen(cmd).read().split('\n')
    svnoutput = map(str.strip, cmd_out)

    # write output to file
    for line in svnoutput:
        if line.startswith("Properties"):
            continue
        if line.startswith("svn:externals"):
            continue
        if line == "":
            continue

        if line in remove_lines:
            continue

        file.write(line + '\n')

    # adds your new line to the end of our tmp file
    file.write(newscriptadd)
    file.close()



    # write everything back to written itmp file to svn:externals
    cmd = "svn propset svn:externals -F " + writefile + " " + svn_client_path + foldername
    cmd_out = os.popen(cmd).read().split('\n')

    print foldername + " written"
